class TestUserRatingAPI(APITestCase):

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
        UserRating.objects.create(user=user, movie=movie,
                                  rate=2)
        UserRating.objects.create(user=user, movie=movie2,
                                  rate=5)

    def test_create_user_rating_post(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        rating_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                       "rate": 4}
        response = self.client.post(reverse('userrating-list'),
                                    data=rating_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='Correct body, should return status 201')

    def test_list_get_user_rating(self):
        self.assertTrue(self.client.login(username='Test',
                                          password='TestPw4foranewuser'))
        response = self.client.get(reverse('userrating-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='Response should return status 200')

    def test_user_rating_for_unauthorized_return_forbidden(self):
        rating_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                       "rate": 4}
        response = self.client.post(reverse('userrating-list'),
                                    data=rating_body,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN,
                         msg='Unauthorized POST should return status 403')

    # def test_get_watchlist_added_only(self):
    #     self.assertTrue(self.client.login(username='Test',
    #                     password='TestPw4foranewuser'))
    #     movie = Movie.objects.get(id=1)
    #     user = User.objects.get(id=1)
    #     watchlist_disable = Watchlist.objects.get(id=1)
    #     watchlist_disable.added = False
    #     watchlist_disable.save()
    #     self.assertTrue(watchlist_disable,
    #                     msg='Watchlist has not been created.')
    #     response = self.client.get(reverse('watchlist-list'))
    #     self.assertEqual(response.data['count'], 1,
    #                      msg='A list should include 2 movies.')

    def test_get_retrive_user_rateing(self):
        user_rating = UserRating.objects.get(id=1)
        response = self.client.get(reverse('userrating-detail',
                                   args=[user_rating.id]))
        self.assertTrue(response)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

    def test_update_user_rating(self):
        rating_body = {"movie": "http://127.0.0.1:8000/api/v1/movies/1/",
                          "added": False}
        url = reverse('userrating-detail', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.put(url, data=rating_body)
        self.assertTrue(response)
        user_rating_list_response = self.client.get(reverse('userrating-list'))
        self.assertEqual(user_rating_list_response.data['count'], 1,
                         msg='A list should include 1 movies.')

        self.assertEqual(user_rating_list_response.status_code,
                         status.HTTP_200_OK)

    def test_delete_user_rating(self):
        url = reverse('userrating-list', kwargs={'pk': 1})
        self.client.login(username='Test', password='TestPw4foranewuser')
        response = self.client.delete(url)
        self.assertTrue(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(UserRating.DoesNotExist):
            UserRating.objects.get(id=1)
