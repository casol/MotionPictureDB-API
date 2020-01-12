from datetime import date
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from mpdb_api.serializers import MovieSerializer
from mpdb_api.models import Movie, Comment, Watchlist, Favorite


User = get_user_model()


class TestGetMovieAPI(APITestCase):
    # test_methodName_withCertainState_shouldDoSomething
    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))

        movie2 = Movie.objects.create(
            title="Toy Story 2", year="2000",
            rated="G", released="22 Nov 2000",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))

    def test_get_all_movies_list(self):
        """Get a list of all movies."""
        response = self.client.get(reverse('movie-list'))
        movies = Movie.objects.all()
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        serializer = MovieSerializer(movies,
                                     context=serializer_context,
                                     many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK,
                         msg='Movie list not in the response.')

    def test_get_movie_retrive(self):
        """Get a movie"""
        movie = Movie.objects.get(id=1)
        response = self.client.get(reverse('movie-detail', args=[movie.id]))
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        serializer = MovieSerializer(movie, context=serializer_context)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_with_wrong_id(self):
        """Get a movie with wrong id"""
        response = self.client.get(reverse('movie-detail', args=['toystory']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestPostMovieAPI(APITestCase):
    """Test movie create, updated and delete methods."""

    def setUp(self):
        self.correct_body = {
            "title": "Saw", "year": "2004", "rated": "R",
            "released": "29 Oct 2004", "runtime": "103 min",
            "genre": "Horror, Mystery, Thriller", "director": "James Wan",
            "writer": "Leigh Whannell, James Wan (story), Leigh Whannell",
            "actors": "Leigh Whannell, Cary Elwes, Danny Glover, Ken Leung",
            "plot": "Two strangers, who awaken in a room with no recollection",
            "language": "English",
            "country": "USA",
            "awards": "8 wins & 10 nominations.",
            "poster": "https://m.media-amazon.com/images/M/SX300.jpg",
            "metascore": "46",
            "imdbrating": "7.6",
            "imdbvotes": "360,395",
            "imdbid": "tt0387564",
            "type": "movie",
            "dvd": "15 Feb 2005",
            "boxoffice": "$55,100,000",
            "production": "Lions Gate Films",
            "website": "N/A",
            "created": "2019-12-29T14:28:26.848043Z",
            "ratings":
            [{"source": "Internet Movie Database", "value": "7.6/10"},
                {"source": "Rotten Tomatoes", "value": "49%"},
                {"source": "Metacritic", "value": "46/100"}], }

    def test_create_incorrect_request_body(self):
        """Request should have all required fields."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        incorrect_body = {'title': 'Snatch'}
        response = self.client.post(reverse('movie-list'), data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         'Incorrect body, should return status 400')

    def test_create_with_post_unauthorized_request(self):
        """Only admin is allow to post a new movie."""
        incorrect_body = {'incorrect_field': 'Snatch'}
        response = self.client.post(reverse('movie-list'), data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         'Incorrect body, should return status 404')

    def test_create_with_correct_body_post_request(self):
        """Only admin should be able to add a new movie."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')

        response = self.client.post(reverse('movie-list'),
                                    data=self.correct_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')
        self.assertTrue(Movie.objects.get(id=1),
                        msg='Movie not added to the database')

    def test_update_put_request(self):
        """Only admin is allow to update."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('/api/v1/movies/', data=self.correct_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')
        updated_body = self.correct_body
        updated_body['title'] = 'new title'
        url = reverse('movie-detail', kwargs={'pk': 1})
        respone_put = self.client.put(url,
                                      data=updated_body,
                                      format='json')
        self.assertEqual(respone_put.status_code, status.HTTP_200_OK,
                         msg='Update should return status 200')


class TestCommentAPI(APITestCase):
    # test_methodName_withCertainState_shouldDoSomething
    @classmethod
    def setUpTestData(cls):
        user_data = ['Test', 'Test@test.com', 'TestPw4foranewuser']
        user = User.objects.create_user(*user_data)
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        comment = Comment.objects.create(user=user, movie=movie,
                                         body='Great Movie!')
        comment2 = Comment.objects.create(user=user, movie=movie,
                                          body='Great Movie!')

    def test_create_comments_post(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        comment_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                        "body": "test comment"}
        response = self.client.post(reverse('comment-list'), data=comment_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')

    def test_get_all_comment_list(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='Response should return status 200')

    def test_post_comment_for_unauthorized_return_forbidden(self):
        comment_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                        "body": "test comment"}
        response = self.client.post(reverse('comment-list'), data=comment_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         msg='Unauthorized POST should return status 403')

    def test_get_comment_active_only(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        movie = Movie.objects.get(id=1)
        user = User.objects.get(id=1)
        comment_inactive = Comment.objects.create(user=user,
                                                  movie=movie,
                                                  body='FU**K Y**',
                                                  active=False)
        self.assertTrue(comment_inactive,
                        msg='Inactive comment has not been created.')
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.data['count'], 2,
                         msg='A list should include 2 comments.')

    def test_retrive_comment_get(self):
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('comment-detail',
                                   args=[comment.id]))
        self.assertTrue(response)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        comment_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                        "url": "http://127.0.0.1:8000/api/v1/comments/1/",
                        "body": "updated comment"}
        url = reverse('comment-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.put(url, data=comment_body)
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        url = reverse('comment-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.delete(url)
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=1)


class TestWatchlistAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_data = ['Test', 'Test@test.com', 'TestPw4foranewuser']
        user = User.objects.create_user(*user_data)
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        movie2 = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        watchlist = Watchlist.objects.create(user=user, movie=movie,
                                             added=True)
        watchlist2 = Watchlist.objects.create(user=user, movie=movie2,
                                              added=True)

    def test_add_to_watchlist_post(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        watchlist_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                          "added": True}
        response = self.client.post(reverse('watchlist-list'),
                                    data=watchlist_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')

    def test_get_all_watchlist_movies(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        response = self.client.get(reverse('watchlist-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='Response should return status 200')

    def test_post_watchlist_for_unauthorized_return_forbidden(self):
        watchlist_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                          "added": True}
        response = self.client.post(reverse('watchlist-list'),
                                    data=watchlist_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         msg='Unauthorized POST should return status 403')

    def test_get_watchlist_added_only(self):
        self.assertTrue(self.client.login(username='Test',
                        password='TestPw4foranewuser'))
        movie = Movie.objects.get(id=1)
        user = User.objects.get(id=1)
        watchlist_disable = Watchlist.objects.get(id=1)
        watchlist_disable.added = False
        watchlist_disable.save()
        self.assertTrue(watchlist_disable,
                        msg='Watchlist has not been created.')
        response = self.client.get(reverse('watchlist-list'))
        self.assertEqual(response.data['count'], 1,
                         msg='A list should include 2 movies.')

    def test_get_retrive_watchlist(self):
        watchlist = Watchlist.objects.get(id=1)
        response = self.client.get(reverse('watchlist-detail',
                                   args=[watchlist.id]))
        self.assertTrue(response)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_update_remove_from_watchlist(self):
        watchlist_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                          "added": False}
        url = reverse('watchlist-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.put(url, data=watchlist_body)
        self.assertTrue(response)
        watchlist_list_response = self.client.get(reverse('watchlist-list'))
        self.assertEqual(watchlist_list_response.data['count'], 1,
                         msg='A list should include 1 movies.')

        self.assertEqual(watchlist_list_response.status_code,
                         status.HTTP_200_OK)

    def test_delete_watchlist(self):
        url = reverse('watchlist-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.delete(url)
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Watchlist.DoesNotExist):
            Watchlist.objects.get(id=1)


class TestFavoriteAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_data = ['Test', 'Test@test.com', 'TestPw4foranewuser']
        user = User.objects.create_user(*user_data)
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        movie2 = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        favorite = Favorite.objects.create(user=user, movie=movie,
                                           added=True)
        favorite2 = Favorite.objects.create(user=user, movie=movie2,
                                            added=True)

    def test_add_to_favorite_movie_post(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        favorite_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                         "added": True}
        response = self.client.post(reverse('favorite-list'),
                                    data=favorite_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')

    def test_get_all_favorite_movies(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        response = self.client.get(reverse('favorite-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='Response should return status 200')

    def test_post_favorite_for_unauthorized_return_forbidden(self):
        favorite_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                         "added": True}
        response = self.client.post(reverse('favorite-list'),
                                    data=favorite_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         msg='Unauthorized POST should return status 403')

    def test_get_favorite_movies_added_only(self):
        self.assertTrue(self.client.login(username='Test',
                        password='TestPw4foranewuser'))
        movie = Movie.objects.get(id=1)
        user = User.objects.get(id=1)
        favorite_disable = Favorite.objects.get(id=1)
        favorite_disable.added = False
        favorite_disable.save()
        self.assertTrue(favorite_disable,
                        msg='Favorite has not been created.')
        response = self.client.get(reverse('favorite-list'))
        self.assertEqual(response.data['count'], 1,
                         msg='A list should include 1 movies.')

    def test_get_retrive_favorite_movie(self):
        favorite = Favorite.objects.get(id=1)
        response = self.client.get(reverse('favorite-detail',
                                   args=[favorite.id]))
        self.assertTrue(response)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_update_favorite_movie(self):
        favorite_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                         "added": False}
        url = reverse('favorite-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.put(url, data=favorite_body)
        self.assertTrue(response)
        response_updated = self.client.get(url)
        self.assertEqual(response_updated.status_code,
                         status.HTTP_404_NOT_FOUND)

    def test_delete_favorite_movie(self):
        url = reverse('favorite-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.delete(url)
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Favorite.DoesNotExist):
            Favorite.objects.get(id=1)


class TestCustomUserAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_data = ['Test', 'Test@test.com', 'TestPw4foranewuser']
        user = User.objects.create_user(*user_data)
        movie = Movie.objects.create(
            title="Toy Story", year="1995",
            rated="G", released="22 Nov 1995",
            runtime="81 min",
            genre="Animation, Adventure, Comedy, Family, Fantasy",
            director="John Lasseter",
            writer="John Lasseter (original story by)",
            actors="Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
            plot="A cowboy doll is profoundly threatened and \
                jealous when a new spaceman figure supplants.",
            language="English", country="USA",
            awards="Nominated for 3 Oscars. Another 23 wins & 17 nominations.",
            poster="https=//m.media-amazon.com/images/I@._V1_SX300.jpg",
            metascore="95",
            imdbrating="8.3", imdbvotes="825,214",
            imdbid="tt0114709", type="movie",
            dvd="20 Mar 2001", boxoffice="N/A",
            production="Buena Vista", website="N/A",
            created=str(date.today()))
        favorite = Favorite.objects.create(user=user, movie=movie,
                                           added=True)
        watchlist = Watchlist.objects.create(user=user, movie=movie,
                                             added=True)
        comment = Comment.objects.create(user=user, movie=movie,
                                         body='WoW!')

    def test_get_list_users(self):
        response = self.client(reverse('customuser-list'))
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # TODO TypeError: 'APIClient' object is not callable
    # def test_get_retrive_users(self):
    #     response = self.client(reverse('customuser-detail',
    #                            kwargs={'username': 'Test'}))
    #     self.assertTrue(response)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateUser(APITestCase):
    """Test user registration."""

    def setUp(self):
        self.data = {'username': 'Test', 'email': 'Test@test.com',
                     'password1': 'TestPw4foranewuser',
                     'password2': 'TestPw4foranewuser'}

    def test_registration_with_post_register_user(self):
        response = self.client.post('/rest-auth/registration/', data=self.data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_get_not_allowed(self):
        response = self.client.get('/rest-auth/registration/', data=self.data,
                                   format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED,
                         msg='Register with get should return status 405')
