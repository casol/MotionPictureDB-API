from django.contrib import admin
from mpdb_api.models import Comment, Movie, Watchlist, Rating


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
