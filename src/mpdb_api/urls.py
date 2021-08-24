from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from mpdb_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'watchlist', views.WatchlistViewSet, basename='watchlist')
router.register(r'favorite', views.FavoriteViewSet, basename='favorite')
router.register(r'rating', views.UserRatingViewSet, basename='userrating')
router.register(r'users', views.CustomUserViewSet)
# The API URLs are determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
