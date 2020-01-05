import requests
from urllib.parse import urljoin


class Client():
    """API Client for the OMDb API.

    An entry point for making request to the OMDb API.
    Provide methods to search data from tue API endpoints.
    """

    API_BASE_URI = 'http://www.omdbapi.com'

    def __init__(self, api_key):
        if not api_key:
            raise ValueError('Missing OMDb api key')
        self.API_KEY = api_key

    def build_api_url(self, *args):
        """Build fine URL endpoint."""
        join_path = ''.join(args)
        return urljoin(self.API_BASE_URI, join_path)

    def _get(self, *args):
        """Build response object, creates a HTTP request."""
        url = self.build_api_url(*args)
        print(url)
        response = requests.get(url)
        return response

    def check_response_status(self, response):
        """Check the response status code and API response status."""
        return (response.status_code == requests.codes.ok and
                response.json()['Response'] == 'True')

    def adjust_to_the_model(self, *args, **kwargs):
        """Adjust API response to match model fields."""
        data = dict((key.lower(), value)
                    for key, value in kwargs.items())
        data['ratings'] = [
                dict((key.lower(), value) for key, value in rating.items())
                for rating in data['ratings']]
        return data

    def search_movie(self, search_terms):
        """Call an API and search for a movie.

        http://www.omdbapi.com/?apikey=[api_key]&t=MovieTitle
        """
        # Character encoding
        print(search_terms)
        search_terms = '%20'.join(search_terms)
        search_response = self._get('?apikey=', self.API_KEY,
                                    '&t=', search_terms)
        if self.check_response_status(search_response):
            return self.adjust_to_the_model(**search_response.json())
