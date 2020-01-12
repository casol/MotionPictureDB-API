from django.db import models
from django.conf import settings


class Movie(models.Model):
    """Stores a single movie entry."""

    title = models.CharField(max_length=200, blank=False)
    year = models.CharField(max_length=4)
    rated = models.CharField(max_length=255)
    released = models.CharField(max_length=255)
    runtime = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    plot = models.TextField()
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    awards = models.CharField(max_length=255)
    poster = models.CharField(max_length=250)
    metascore = models.CharField(max_length=255)
    imdbrating = models.CharField(max_length=255)
    imdbvotes = models.CharField(max_length=255)
    imdbid = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    dvd = models.CharField(max_length=255)
    boxoffice = models.CharField(max_length=255)
    production = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'(id:{self.id}) {self.title}'


class Rating(models.Model):
    """Stores a movie rating."""

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="ratings")
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.source}: {self.value}'


class Comment(models.Model):
    """User comments model."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='comments',
                             on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movies',
                              on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Comment by {self.user} on {self.movie}'


class Watchlist(models.Model):
    """Stores a user watchlist."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='watchlist',
                             on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='watchlist',
                              on_delete=models.CASCADE)
    added = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.movie}: {self.added}'


class Favorite(models.Model):
    """Stores a list of favorite movies."""

    movie = models.ForeignKey(Movie, related_name="favorites",
                              on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="favorites",
                             on_delete=models.CASCADE)
    added = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.movie}'
