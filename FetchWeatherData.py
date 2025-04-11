import urllib.request, urllib.parse
from urllib.error import HTTPError, URLError
import logging
import sys

class FetchWeatherData:
    """
    Takes latitude and longitude and returns the raw data from 
    locationforecast. lat and lon default to roughly the center of Oslo.
    """

    LOGGER = logging.getLogger(__name__)
    API_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"


    def get(coord):
        # Do the request and return raw json
        vals = {"lat" : coord[0], "lon" : coord[1]}
        data = urllib.parse.urlencode(vals)
        url = FetchWeatherData.API_URL + '?' + data

        FetchWeatherData.LOGGER.debug('Sending request to {}\n'.format(url))
        req = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla'})

        try:
            response = urllib.request.urlopen(req)
            return response.read()
        except URLError as e:
            logging.error('Could not connect to url: {}'.format(e.reason))
            sys.exit(1)
        except HTTPError as e:
            logging.error('Could not retrieve response: {}'.format(e.reason))
            sys.exit(1)