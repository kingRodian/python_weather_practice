import urllib.parse
import urllib.request
import logging

class FetchWeatherData:
    """
    Something something
    """

    LOGGER = logging.getLogger(__name__)
    logging.basicConfig()
    LOGGER.setLevel(logging.DEBUG)

    API_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    DEFAULT_LAT = "59.92"
    DEFAULT_LON = "10.75"

    def get(self, lat=DEFAULT_LAT, lon=DEFAULT_LON):
        self.LOGGER.info('Attempting to send a request to {} with lat: {} and lon: {}\n'.format(self.API_URL, lat, lon))
        vals = {"lat" : lat, "lon" : lon}
        data = urllib.parse.urlencode(vals)
        #data = data.encode('ascii') # Needs to be bytes
        url = self.API_URL + '?' + data
        self.LOGGER.info('{}'.format(url))
        req = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla'})

        with urllib.request.urlopen(req) as response:
            return response.read()