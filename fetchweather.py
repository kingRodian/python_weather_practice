import logging
import sys
from getopt import getopt
from datetime import date, timedelta

from FetchWeatherData import FetchWeatherData
from JSONtoTimeSeries import JSONtoTimeSeries
from CLIOptions import CLIOptions
from LoadCities import LoadCities

# We dont use this for anything atm
LOGGER = logging.getLogger('fetchweather')
logging.basicConfig()



# TODO:
#       Save the entire dataset to a file and check before fetching
#           in order to avoid lots of API calls

def main():
    # Parse options
    opts = CLIOptions(sys.argv)
    location = ''
    coord = ''
    data = ''

    # If there's a coord we use that, else we use the city name
    if opts.coord:
        location = 'Coord:' + str(opts.coord)
        coord = opts.coord
    elif opts.city:
        location = opts.city.capitalize()
        cityLoader = LoadCities()
        cities = cityLoader.get_cities()
        if opts.city.lower() in cities:
            coord = cities[opts.city.lower()]
        else:
            LOGGER.error('Location {} not in database.'.format(opts.city))
            sys.exit(1)
    if not coord:
        LOGGER.error('Could not retrieve location.')
        sys.exit(1)

    data = FetchWeatherData.get(coord)
    timeseries = JSONtoTimeSeries.create_timeseries(data, location)
    timeseries.print_days(opts.days)


main()