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
    timeseries = json_to_time.create_timeseries(data)

    for time, series in timeseries.get_timeseries().items():
        print('Series for date: {}'.format(time.date()))
        for timepoint in series:
            print(timepoint)


main()