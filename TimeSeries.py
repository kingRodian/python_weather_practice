import logging
from datetime import datetime

class TimeSeries:
    """
    Holds a dict of dates to lists of timepoints,
    where TimePoint holds weather data for a particular hour. 
    Methods for adding timepoints etc
    """

    def __init__(self):
        self.timepoints = dict()


    def add_timepoint(self, timepoint):
        day = datetime.combine(timepoint.time.date())
        if day in self.timepoints:
            daylist = self.timepoints[day]
            daylist.append(timepoint)
        else:
            self.timepoints[day] = [timepoint]
        
    def get_timeseries(self):
        return self.timepoints

    def get_timepoints(self, day):
        return self.timepoints[day] if day in timepoints else []

    # Implement __repr__ to print the timeseries date by date




