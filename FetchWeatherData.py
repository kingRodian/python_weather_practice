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

    def get(lat=DEFAULT_LAT, lon=DEFAULT_LON):
        # Do the request and return raw json
        vals = {"lat" : lat, "lon" : lon}
        data = urllib.parse.urlencode(vals)
        url = FetchWeatherData.API_URL + '?' + data

        FetchWeatherData.LOGGER.debug('Sending request to {}\n'.format(url))
        req = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla'})

        with urllib.request.urlopen(req) as response:
            return response.read()