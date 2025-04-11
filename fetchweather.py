import logging
from datetime import date, timedelta

from FetchWeatherData import FetchWeatherData
from JSONtoTimeSeries import JSONtoTimeSeries

# We dont use this for anything atm
LOGGER = logging.getLogger(__name__)
logging.basicConfig()

# TODO: Add functionality to enter coords and date
#       Save the entire dataset to a file and check before fetching
#           in order to avoid lots of API calls

def main():
    data = FetchWeatherData.get()
    timeseries = JSONtoTimeSeries.create_timeseries(data)
    # For the moment we print for tomorrow
    tomorrow = date.today() + timedelta(days=1)
    timeseries.print_date(tomorrow)


main()