from datetime import date
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from mpdb_api.serializers import MovieSerializer, CustomUserSerializer
from mpdb_api.models import Movie


User = get_user_model()


class GetMovieAPITest(APITestCase):

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

    def test_get_all_movies(self):
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

    def test_get_movie(self):
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


class PostMovieAPITest(APITestCase):
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

    def test_incorrect_request_body(self):
        """Request should have all required fields."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        incorrect_body = {'title': 'Snatch'}
        response = self.client.post('/api/v1/movies/', data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         'Incorrect body, should return status 400')

    def test_unauthorized_request(self):
        """Only admin is allow to post a new movie."""
        incorrect_body = {'incorrect_field': 'Snatch'}
        response = self.client.post('/api/v1/movies/', data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         'Incorrect body, should return status 404')

    def test_correct_post_request(self):
        """Only admin should be able to add a new movie."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')

        response = self.client.post('/api/v1/movies/', data=self.correct_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')
        self.assertTrue(Movie.objects.get(id=1),
                        msg='Movie not added to the database')

    def test_put_request(self):
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
        respone_put = self.client.put('/api/v1/movies/1/',
                                      data=updated_body,
                                      format='json')
        self.assertEqual(respone_put.status_code, status.HTTP_200_OK,
                         msg='Update should return status 200')


class CreateUserTest(APITestCase):

    def setUp(self):
        #self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       #'johnpassword')
        #self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'Test', 'email': 'Test@test.com',
                     'password1': 'qwert', 'password2': 'qwert'}

    def test_can_create_user(self):
        # todo
        response = self.client.post('/rest-auth/registration/', data=self.data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
