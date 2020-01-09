from rest_framework import serializers

from users.models import CustomUser
from mpdb_api.models import Movie, Comment, Watchlist, Rating, Favorite


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for user list of favorite movies."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Favorite
        fields = ('user', 'movie', 'url', 'added')


class WatchlistSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for a user watchlist."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Watchlist
        fields = ('movie', 'user', 'added', 'url')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for user comments."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('movie', 'user', 'body', 'url')


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for a custom user model with related user action."""

    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name='comment-detail', read_only=True)

    url = serializers.HyperlinkedIdentityField(
        view_name='customuser-detail', lookup_field='username')

    watchlist = serializers.HyperlinkedRelatedField(
        many=True, view_name='movie-detail', read_only=True)

    favorites = serializers.HyperlinkedRelatedField(
        many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'id', 'username',
                  'comments', 'watchlist', 'favorites')


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for a movie rating."""

    class Meta:
        model = Rating
        fields = ("source", "value")


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for movies."""

    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        """Writable nested serializers for movie ratings."""
        ratings_data = validated_data.pop('ratings')
        movie = Movie.objects.create(**validated_data)
        # Iterate over ratings
        for rating_data in ratings_data:
            Rating.objects.create(movie=movie, **rating_data)
        return movie

    def update(self, instance, validated_data):
        """Updatable nested serializer for movie ratings."""
        ratings_data = validated_data.pop('ratings')
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        # Update ratings instances that are in the request
        for rating in instance.ratings.all():
            for new_rating in ratings_data:
                if rating.source == new_rating['source']:
                    rating.value = new_rating['value']
                    rating.save()
        return instance
