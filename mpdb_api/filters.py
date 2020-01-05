import operator
from functools import reduce
from django.db import models
from django.conf import settings

from rest_framework import filters
from rest_framework.compat import distinct

from mpdb_api.services import Client
from mpdb_api.serializers import MovieSerializer
from mpdb_api.models import Movie


class CustomSearchFilter(filters.SearchFilter):
    """"Dynamically change search fields based on request content."""

    def get_search_fields(self, view, request):
        """
        Search only on title if the query parameter
        title_only is in the request
        """
        if 'title' in request.query_params:
            return ['title']
        elif 'genre' in request.query_params:
            return ['genre']
        return super(CustomSearchFilter, self).get_search_fields(view, request)

    def filter_queryset(self, request, queryset, view):
        """
        Check if the title exist in the local database or send
        a request to the OMDb API and save to the local database.
        """
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)
        print(search_terms)
        if not search_fields or not search_terms:
            return queryset

        orm_lookups = [
            self.construct_search(str(search_field))
            for search_field in search_fields
        ]
        base = queryset
        conditions = []
        for search_term in search_terms:
            queries = [
                models.Q(**{orm_lookup: search_term})
                for orm_lookup in orm_lookups
            ]
            conditions.append(reduce(operator.or_, queries))
        queryset = queryset.filter(reduce(operator.and_, conditions))

        if self.must_call_distinct(queryset, search_fields):
            # Filtering against a many-to-many field requires us to
            # call queryset.distinct() in order to avoid duplicate items
            # in the resulting queryset.
            # We try to avoid this if possible, for performance reasons.
            queryset = distinct(queryset, base)
        print(queryset.exists())
        if queryset.exists():
            return queryset
        else:
            # Create client instance
            client = Client(settings.OMDB_API_KEY)
            data = client.search_movie(search_terms)
            serializer_context = {'request': request, }
            serializer = MovieSerializer(data=data, context=serializer_context)
            if serializer.is_valid():
                movie = serializer.save()
                # queryset = Movie.objects.filter(title__icontains=search_terms)
                queryset = Movie.objects.filter(id=movie.id)
                return queryset
            else:
                # If move does not exist return empty queryset
                return queryset
