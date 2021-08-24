from django.contrib import admin
from mpdb_api.models import (Comment, Movie, Watchlist,
                             Rating, Favorite, UserRating)


class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rate')


admin.site.register(UserRating, UserRatingAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added')


admin.site.register(Favorite, FavoriteAdmin)


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added')


admin.site.register(Watchlist, WatchlistAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)


class RatingInline(admin.TabularInline):
    model = Rating


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        RatingInline,
    ]


admin.site.register(Movie, MovieAdmin)
