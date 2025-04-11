import logging
from datetime import datetime

class TimeSeries:
    """
    Holds a dict of dates to lists of timepoints,
    where TimePoint holds weather data for a particular hour. 
    Methods for adding timepoints etc
    """

    TOP_REPR_FMT = 'Temperatures for {location} {date}:\n'

    def __init__(self, location):
        self.timepoints = dict()
        self.location = location

    def add_timepoint(self, timepoint):
        # Add a timepoint to the approprate date-list
        day = timepoint.time.date()
        if day in self.timepoints:
            daylist = self.timepoints[day]
            daylist.append(timepoint)
        else:
            self.timepoints[day] = [timepoint]
        
    def get_timeseries(self):
        # Return the whole dict
        return self.timepoints

    def get_timepoints(self, date):
        # Return list for certain date
        return self.timepoints[date] if date in timepoints else []

    def str_timepoints_date(self, date):
        # Return timepoints for a certain date as a printable string
        output = self.TOP_REPR_FMT.format(location=self.location, date=date.isoformat())
        for point in self.timepoints[date]:
            output += str(point)
            output += '\n'
        return output

    def print_date(self, date):
        print(self.str_timepoints_date(date))

    def __repr__(self):
        # Print out the entire timeseries
        output = ''
        for date in sorted(self.timepoints.keys()):
            output += self.str_timepoints_date(date) + '\n'
        return output
