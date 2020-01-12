# MotionPictureDB API
*in progress*

MotionPictureDB a Web API for viewing, searching, commenting, rating and saving your favorite movies build with Django REST framework.
It is based on the external OMDB API for searching (and saving locally) movies and making them available to api users.
The application extends its capabilities by setting up an account, logging in, rating movies, commenting, creating a list of favorite movies and watchlist.

## TODO
* user rating

## API Guide 
**Routers** /api/v1/

Registration /rest-auth/registration/
 
**Login**
/rest-auth/login/

**Logout**
/rest-auth/logout/
## Endpoints
Full documentation can be found at http://127.0.0.1:8000/docs/

and
short version below:

**GET** /api/v1/movies/

Return a list of all the existing movies (page size 10).

**GET** SEARCH /api/v1/movies/?search={movie title}&title

Check if the title exist in the local database or send
a request to the OMDb API and save to the local database.

**GET SEARCH** /api/v1/movies/?search={genre}&genre

Search by genre on the local database.

**GET** /api/v1/movies/{id}/

Return the given movie.

**POST** /api/v1/movies/

Create a new movie instance (admin only).

**GET** /api/v1/users/

Return a list of all the existing users with all profile details.

**GET** /api/v1/users/{username}/

Return the given user with user's watchlist, favorites, comments and movie ratings.

**GET** /api/v1/comments/

Return a list of all the existing comments.

**POST** /api/v1/comments/

Create a new comment instance (authenticated only).

**GET** /api/v1/favorite/

Return a list of all favorite movies for authenticated user. 

**POST** /api/v1/favorite/
Add to favorite (authenticated only).

**GET** /api/v1/watchlist/
Return a list of all movies in the watchlist for authenticated user.

**POST** /api/v1/watchlist/
Add to watchlist.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - The web framework used


## Authors

*  *Initial work* - [casol](https://github.com/casol)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/casol/MotionPictureDB-API/blob/master/LICENSE.md) file for details