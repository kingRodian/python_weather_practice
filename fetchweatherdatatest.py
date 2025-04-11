from FetchWeatherData import FetchWeatherData
from JSONtoTimeSeries import JSONtoTimeSeries

fetcher = FetchWeatherData()
json_to_time = JSONtoTimeSeries()





def main():
    # data = fetcher.get()
    # timeseries = json_to_time.create_timeseries()
    data = ''
    with open('examplejson.json', 'r') as f:
        data = f.read()
    timeseries = JSONtoTimeSeries().create_timeseries(data)

    print(str(timeseries))


main()