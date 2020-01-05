from datetime import date
from django.test import TestCase
from mpdb_api.models import Movie, Comment, Rating, Watchlist, Favorite
from django.contrib.auth import get_user_model


class MovieModelTest(TestCase):
    """Test movie model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a movie with related objects."""
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min", genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter", writer="John Lasseter (original story by), Pete Docter (original story by), \
                Andrew Stanton (original story by), Joe Ranft (original story by),\ Joss Whedon (screenplay by), \
                Andrew Stanton (screenplay by), Joel Cohen (screenplay by), Alec Sokolow (screenplay by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney", plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants him as top toy in a boy's room.",
            language="English", country="USA", awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg", metascore="95",
            imdbrating= "8.3", imdbvotes="825,214",
            imdbid= "tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice= "N/A",
            production= "Buena Vista", website="N/A",
            created= str(date.today()))

    def test_title_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_year_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('year').verbose_name
        self.assertEqual(field_label, 'year')

    def test_rated_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('rated').verbose_name
        self.assertEqual(field_label, 'rated')

    def test_released_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('released').verbose_name
        self.assertEqual(field_label, 'released')

    def test_runtime_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('runtime').verbose_name
        self.assertEqual(field_label, 'runtime')

    def test_genre_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_director_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('director').verbose_name
        self.assertEqual(field_label, 'director')

    def test_writer_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('writer').verbose_name
        self.assertEqual(field_label, 'writer')

    def test_actors_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('actors').verbose_name
        self.assertEqual(field_label, 'actors')

    def test_plot_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('plot').verbose_name
        self.assertEqual(field_label, 'plot')

    def test_language_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_country_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_awards_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('awards').verbose_name
        self.assertEqual(field_label, 'awards')

    def test_poster_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('poster').verbose_name
        self.assertEqual(field_label, 'poster')

    def test_metascore_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('metascore').verbose_name
        self.assertEqual(field_label, 'metascore')

    def test_imdbrating_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('imdbrating').verbose_name
        self.assertEqual(field_label, 'imdbrating')

    def test_imdbvotes_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('imdbvotes').verbose_name
        self.assertEqual(field_label, 'imdbvotes')

    def test_imdbid_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('imdbid').verbose_name
        self.assertEqual(field_label, 'imdbid')

    def test_type_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_dvd_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('dvd').verbose_name
        self.assertEqual(field_label, 'dvd')

    def test_boxoffice_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('boxoffice').verbose_name
        self.assertEqual(field_label, 'boxoffice')

    def test_production_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('production').verbose_name
        self.assertEqual(field_label, 'production')

    def test_website_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('website').verbose_name
        self.assertEqual(field_label, 'website')

    def test_created_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_title_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_year_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('year').max_length
        self.assertEqual(max_length, 4)

    def test_rated_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('rated').max_length
        self.assertEqual(max_length, 255)

    def test_released_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('released').max_length
        self.assertEqual(max_length, 255)

    def test_runtime_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('runtime').max_length
        self.assertEqual(max_length, 255)

    def test_genre_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('genre').max_length
        self.assertEqual(max_length, 255)

    def test_director_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('director').max_length
        self.assertEqual(max_length, 255)

    def test_writer_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('writer').max_length
        self.assertEqual(max_length, 255)

    def test_actors_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('actors').max_length
        self.assertEqual(max_length, 255)

    def test_language_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('language').max_length
        self.assertEqual(max_length, 255)

    def test_country_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('country').max_length
        self.assertEqual(max_length, 255)

    def test_awards_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('awards').max_length
        self.assertEqual(max_length, 255)

    def test_poster_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('poster').max_length
        self.assertEqual(max_length, 250)

    def test_metascore_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('metascore').max_length
        self.assertEqual(max_length, 255)

    def test_imdbrating_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('imdbrating').max_length
        self.assertEqual(max_length, 255)

    def test_imdbvotes_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('imdbvotes').max_length
        self.assertEqual(max_length, 255)

    def test_imdbid_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('imdbid').max_length
        self.assertEqual(max_length, 255)

    def test_type_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('type').max_length
        self.assertEqual(max_length, 255)

    def test_dvd_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('dvd').max_length
        self.assertEqual(max_length, 255)

    def test_boxoffice_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('boxoffice').max_length
        self.assertEqual(max_length, 255)

    def test_production_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('production').max_length
        self.assertEqual(max_length, 255)

    def test_website_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('website').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_id_colon_movie_title(self):
        movie = Movie.objects.get(id=1)
        expected_name = f'(id:{movie.id}) {movie.title}'
        self.assertEqual(expected_name, str(movie))


class RatingModelTest(TestCase):
    """Test rating model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a movie with related objects."""
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min", genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter", writer="John Lasseter (original story by), Pete Docter (original story by), \
                Andrew Stanton (original story by), Joe Ranft (original story by),\ Joss Whedon (screenplay by), \
                Andrew Stanton (screenplay by), Joel Cohen (screenplay by), Alec Sokolow (screenplay by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney", plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants him as top toy in a boy's room.",
            language="English", country="USA", awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg", metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        ratings = Rating.objects.create(movie=movie, source='Internet Movie Database', value='8.3/10')

    def test_movie_label(self):
        rating = Rating.objects.get(id=1)
        field_label = rating._meta.get_field('movie').verbose_name
        self.assertEqual(field_label, 'movie')

    def test_source_label(self):
        rating = Rating.objects.get(id=1)
        field_label = rating._meta.get_field('source').verbose_name
        self.assertEqual(field_label, 'source')

    def test_value_label(self):
        rating = Rating.objects.get(id=1)
        field_label = rating._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')

    def test_source_max_length(self):
        rating = Rating.objects.get(id=1)
        max_length = rating._meta.get_field('source').max_length
        self.assertEqual(max_length, 255)

    def test_value_max_length(self):
        rating = Rating.objects.get(id=1)
        max_length = rating._meta.get_field('value').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_source_colon_value(self):
        rating = Rating.objects.get(id=1)
        expected_name = f'{rating.source}: {rating.value}'
        self.assertEqual(expected_name, str(rating))


class CommentModelTest(TestCase):
    """Test comment model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a movie with related comment object."""
        User = get_user_model()
        user = User.objects.create_user(username='TestNormal', email='normal@user.com', password='foo')
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min", genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter", writer="John Lasseter (original story by), Pete Docter (original story by), \
                Andrew Stanton (original story by), Joe Ranft (original story by),\ Joss Whedon (screenplay by), \
                Andrew Stanton (screenplay by), Joel Cohen (screenplay by), Alec Sokolow (screenplay by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney", plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants him as top toy in a boy's room.",
            language="English", country="USA", awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg", metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice= "N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        ratings = Rating.objects.create(
            movie=movie, source='Internet Movie Database', value='8.3/10')
        # Create 4 comment objects
        for comment_id in range(1,5):
            comment = Comment.objects.create(
                user=user, movie=movie, body=f'a movie comment nr:{comment_id}',
                created=date.today(), active=True)

    def test_movie_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('movie').verbose_name
        self.assertEqual(field_label, 'movie')

    def test_user_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_body_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_created_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_active_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('active').verbose_name
        self.assertEqual(field_label, 'active')

    def test_active_default_value(self):
        comment = Comment.objects.get(id=1)
        default = comment._meta.get_field('active')
        self.assertTrue(default.get_default())

    def test_object_name_is_user_and_movie(self):
        comment = Comment.objects.get(id=1)
        expected_name = f'Comment by {comment.user} on {comment.movie}'
        self.assertEqual(expected_name, str(comment))


class WatchlistModelTest(TestCase):
    """Test watchlist model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a movie and user with for a watchlist."""
        User = get_user_model()
        user = User.objects.create_user(username='TestNormal', email='normal@user.com', password='foo')
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min", genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter", writer="John Lasseter (original story by), Pete Docter (original story by), \
                Andrew Stanton (original story by), Joe Ranft (original story by),\ Joss Whedon (screenplay by), \
                Andrew Stanton (screenplay by), Joel Cohen (screenplay by), Alec Sokolow (screenplay by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney", plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants him as top toy in a boy's room.",
            language="English", country="USA", awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg", metascore="95",
            imdbrating= "8.3", imdbvotes="825,214",
            imdbid= "tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice= "N/A",
            production= "Buena Vista", website="N/A",
            created= str(date.today()))

        watchlist = Watchlist.objects.create(user=user, movie=movie, added=True, created= str(date.today()))

    def test_movie_label(self):
        watchlist = Watchlist.objects.get(id=1)
        field_label = watchlist._meta.get_field('movie').verbose_name
        self.assertEqual(field_label, 'movie')

    def test_user_label(self):
        watchlist = Watchlist.objects.get(id=1)
        field_label = watchlist._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_added_label(self):
        watchlist = Watchlist.objects.get(id=1)
        field_label = watchlist._meta.get_field('added').verbose_name
        self.assertEqual(field_label, 'added')

    def test_added_default_value(self):
        watchlist = Watchlist.objects.get(id=1)
        default = watchlist._meta.get_field('added')
        self.assertFalse(default.get_default())

    def test_added_object_value(self):
        watchlist = Watchlist.objects.get(id=1)
        added_true = watchlist.added
        self.assertTrue(added_true)

    def test_object_name_is_movie_colon_added(self):
        watchlist = Watchlist.objects.get(id=1)
        expected_name = f'{watchlist.movie}: {watchlist.added}'
        self.assertEqual(expected_name, str(watchlist))


class FavoriteModelTest(TestCase):
    """Test favorite model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a movie and user with for a watchlist."""
        User = get_user_model()
        user = User.objects.create_user(username='TestNormal',
                                        email='normal@user.com',
                                        password='foo')
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min", genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter", writer="John Lasseter (original story by), Pete Docter (original story by), \
                Andrew Stanton (original story by), Joe Ranft (original story by),\ Joss Whedon (screenplay by), \
                Andrew Stanton (screenplay by), Joel Cohen (screenplay by), Alec Sokolow (screenplay by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney", plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants him as top toy in a boy's room.",
            language="English", country="USA", awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg", metascore="95",
            imdbrating= "8.3", imdbvotes="825,214",
            imdbid= "tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice= "N/A",
            production= "Buena Vista", website="N/A",
            created= str(date.today()))

        favorite = Favorite.objects.create(user=user, movie=movie, added=True, created= str(date.today()))

    def test_movie_label(self):
        favorite = Favorite.objects.get(id=1)
        field_label = favorite._meta.get_field('movie').verbose_name
        self.assertEqual(field_label, 'movie')

    def test_user_label(self):
        favorite = Favorite.objects.get(id=1)
        field_label = favorite._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_added_label(self):
        favorite = Favorite.objects.get(id=1)
        field_label = favorite._meta.get_field('added').verbose_name
        self.assertEqual(field_label, 'added')

    def test_added_default_value(self):
        favorite = Favorite.objects.get(id=1)
        default = favorite._meta.get_field('added')
        self.assertFalse(default.get_default())

    def test_added_object_value(self):
        favorite = Favorite.objects.get(id=1)
        added_true = favorite.added
        self.assertTrue(added_true)

    def test_object_name_is_movie_colon_added(self):
        favorite = Favorite.objects.get(id=1)
        expected_name = f'{favorite.movie}'
        self.assertEqual(expected_name, str(favorite))