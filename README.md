# MotionPictureDB API
*in progress*

MotionPictureDB a Web API for viewing, searching, commenting, rating and saving your favorite movies build with Django REST framework.

It is based on the external OMDB API for searching (and saving locally) movies and making them available to api users.
The OMDb API bridge allows you to quickly populate local database with movies from external API. The application extends its capabilities by setting up an account, logging in, rating movies, commenting, creating a list of favorite movies and watchlist.

## API Guide 
**API documentation** /docs/

**Routers** /api/v1/

**Registration** /rest-auth/registration/
 
**Login**
/rest-auth/login/

**Logout**
/rest-auth/logout/

## Endpoints
Full coreapi documentation can be found at docs/ or as a json dump of the current documentation [here](https://github.com/casol/MotionPictureDB-API/blob/master/mpdb_api_docs.json).

and
short version below:

Movie | Description
------------ | -------------
|**GET** /api/v1/movies/ | Return a list of all the existing movies (page size 10)|
|**GET SEARCH** /api/v1/movies/?search={movie title}&title | Check if the title exist in the local database or send a request to the OMDb API and save to the local database.|
|**GET SEARCH** /api/v1/movies/?search={genre}&genre | Search by genre on the local database.|
|**GET** /api/v1/movies/{id}/ | Return the given movie.
|**POST** /api/v1/movies/ | Create a new movie instance (admin only).|

***

Users | Description
------------ | -------------
|**GET** /api/v1/users/ | Return a list of all the existing users with all profile details e.g. watchlist, favorties. |
|**GET** /api/v1/users/{username}/ | Return the given user with user's watchlist, favorites, comments and movie ratings. |

***

Comments | Description
------------ | -------------
|**GET** /api/v1/comments/ | Return a list of all the existing comments. |
|**POST** /api/v1/comments/ | Create a new comment instance (authenticated only). |

***

Favorite | Description
------------ | -------------
|**GET** /api/v1/favorite/ | Return a list of all favorite movies for authenticated user. |
|**POST** /api/v1/favorite/ | Add to favorite (authenticated only). |

***
Watchlist | Description
------------ | -------------
|**GET** /api/v1/watchlist/ | Return a list of all movies in the watchlist for authenticated user. |
|**POST** /api/v1/watchlist/ |Add to watchlist.|

***

Watchlist | Description
------------ | -------------
|**GET** /api/v1/rating/ | Return a list of all rated movies. |
|**POST** /api/v1/rating/ | Rate a movie. |


## OMDb API KEY

The application uses data from the OMDb API.

>The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.

Get an API key --> http://www.omdbapi.com/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing (Linux)

Try it locally:

Download or "git clone" the package:
```
$ git clone https://github.com/casol/MotionPictureDB-API
$ cd MotionPictureDB-API
```
First install the module, preferably in a virtual environment:
```
$ python3 -m venv env
# activate virtual environment
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```
Initiate the migration and then migrate the database:
```
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```
Create an admin user:
```
(env) $ python manage.py createsuperuser
```
Setup OMDb API Key:
```
(env) $ export OMDB_API_KEY=your_key
```
or update settings.py
```
OMDB_API_KEY = your_key
```
Setup a local server:
```
(env) $ python manage.py runserver
```


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - The rest framework used


## Authors

*  *Initial work* - [casol](https://github.com/casol)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/casol/MotionPictureDB-API/blob/master/LICENSE.md) file for details