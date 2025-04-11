from TimePoint import TimePoint
from TimeSeries import TimeSeries
from datetime import datetime
import json


# Example datetime str from the json
# 2025-04-10T07:00:00Z

# Note, json objects need "" for property names
class JSONtoTimeSeries:
    def __init__(self):
        pass

    def create_timeseries(self, jsontext):
        timeseries = TimeSeries()
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
