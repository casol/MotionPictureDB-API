from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from mpdb_api.serializers import CustomUserSerializer

User = get_user_model()


class PostMovieAPITest(APITestCase):

    def test_incorrect_request_body(self):
        """Request should have all required fields."""
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        incorrect_body = {'stuff': 'Snatch'}
        response = self.client.post('/api/v1/movies/', data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         'Incorrect body, should return status 400')

    def test_unauthorized_request_body(self):
        """Only admin is allow to post a new movie."""
        incorrect_body = {'stuff': 'Snatch'}
        response = self.client.post('/api/v1/movies/', data=incorrect_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         'Incorrect body, should return status 404')


# class CreateUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com',
#                                                        'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.data = {'username': 'mike', 'first_name': 'Mike',
#                      'last_name': 'Tyson'}

#     def test_can_create_user(self):
#         response = self.client.post(reverse('user-list'), self.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


