from rest_framework import permissions, viewsets

from mpdb_api.filters import CustomSearchFilter
from users.models import CustomUser
from mpdb_api.models import Comment, Movie, Watchlist, Favorite
from mpdb_api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from mpdb_api.serializers import (
    CommentSerializer, CustomUserSerializer,
    MovieSerializer, WatchlistSerializer, FavoriteSerializer)


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all favorite movies.

    retrieve:
    Return a favorite movie details.

    create:
    Add movie to favorite.

    update:
    Update favorite movie list.
    """

    serializer_class = FavoriteSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def get_queryset(self):
        """
        This view should return a list of all the favorite movies
        for the currently authenticated user.
        """
        user = self.request.user
        # Filtering against the current user
        return Favorite.objects.filter(user=user.id, added=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WatchlistViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all movies in the watchlist.

    retrieve:
    Return a given watchlist movie.

    create:
    Add movie to a watchlist.

    update:
    Update watchlist.
    """

    serializer_class = WatchlistSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def get_queryset(self):
        """
        This view should return a list of all the movies from
        the watchlist for the currently authenticated user.
        """
        user = self.request.user
        return Watchlist.objects.filter(user=user.id, added=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing comments.

    retrieve:
    Return the given comment.

    create:
    Create a new comment instance.

    update:
    Update a comment body.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return the given user with user's watchlist, favorites,
    comments and movie ratings.

    list:
    Return a list of all the existing users.
    """

    queryset = CustomUser.objects.all()
    lookup_field = 'username'
    serializer_class = CustomUserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given movie.

    list:
    Return a list of all the existing movies.

    create:
    Create a new movie instance.

    search:
    Search for a movie in the local database or
    send search request to the OMDb API.
    Search for a movie /api/v1/movies/?search=ring&title
    Search by genre /api/v1/movies/?search=horror&genre
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [CustomSearchFilter]
    search_fields = ['title', 'genre']
