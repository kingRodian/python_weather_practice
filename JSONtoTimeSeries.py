from TimePoint import TimePoint
from TimeSeries import TimeSeries
from datetime import datetime
import json

class JSONtoTimeSeries:
    """
    Converts JSON from locationforecast API to a TimeSeries
    class holding a dict of lists of TimePoints.

    The data we want from the JSON is the properties.timeseries,
    which is a list of times and data. The data we want from these are
    time and data.instant.details which contains temp, humidity etc.
    We also want the precipitation for that hour, which is not in the instant, but next 1 hour
    """

    def create_timeseries(jsontext, location):
        timeseries = TimeSeries(location)
        data = json.loads(jsontext)
        try:
            for val in data['properties']['timeseries']:
                details = val['data']['instant']['details']
                time = datetime.fromisoformat(val['time'])
                precipitation = val['data']['next_1_hours']['details']['precipitation_amount']
                timepoint = TimePoint(time=time, precipitation=precipitation, **details)
                timeseries.add_timepoint(timepoint)
                
        except Exception as e:
            # Add expection handling
            pass
        return timeseries
