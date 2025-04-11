import urllib.parse
import urllib.request
import logging

class FetchWeatherData:
    """
    Takes latitude and longitude and returns the raw data from 
    locationforecast. lat and lon default to roughly the center of Oslo.
    """

    LOGGER = logging.getLogger(__name__)
    API_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    DEFAULT_LAT = "59.92"
    DEFAULT_LON = "10.75"

    def get(self, lat=DEFAULT_LAT, lon=DEFAULT_LON):
        vals = {"lat" : lat, "lon" : lon}
        data = urllib.parse.urlencode(vals)
        url = self.API_URL + '?' + data

        self.LOGGER.debug('Sending request to {}\n'.format(url))
        req = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla'})

        with urllib.request.urlopen(req) as response:
            return response.read()