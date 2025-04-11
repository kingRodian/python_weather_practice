from TimePoint import TimePoint
from TimeSeries import TimeSeries
from datetime import datetime
import json

class JSONtoTimeSeries:
    """
    Converts JSON from locationforecast to a TimeSeries
    class holding lists of TimePoints.

    The data we want from the JSON is the properties.timeseries,
    which is a list of times and data. The data we want from these are
    time and data.instant.details which contains temp, humidity etc.
    """

    def create_timeseries(self, jsontext, location='Oslo'):
        timeseries = TimeSeries(location)
        data = json.loads(jsontext)
        try:
            for val in data['properties']['timeseries']:
                details = val['data']['instant']['details']
                time = datetime.fromisoformat(val['time'])
                timepoint = TimePoint(time=time, **details)
                timeseries.add_timepoint(timepoint)
                
        except Exception as e:
            # Add expection handling
            pass
        return timeseries
