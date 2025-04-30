import logging
import datetime

class TimeSeries:
    """
    Holds a dict of dates to lists of timepoints,
    where TimePoint holds weather data for a particular hour. 
    Methods for adding timepoints etc
    """

    TOP_REPR_FMT = 'Temperatures for {location} {date}:\n'
    AVGS_FMT = '''Averages:
00:00-08:00 - {}
08:00-12:00 - {}
12:00-18:00 - {}
18:00-00:00 - {}
'''
    AVG_RANGES = [(0, 8), (8, 12), (12, 18), (18, 23)]

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
        return self.timepoints[date] if date in self.timepoints else []

    def str_timepoints_date(self, date, precipitation=False):
        # Return timepoints for a certain date as a printable string
        output = self.TOP_REPR_FMT.format(location=self.location, date=date.isoformat())
        tot_avg = 0
        points = self.timepoints[date]
        for point in points:
            tot_avg = tot_avg + point.temperature()
            output += str(point)
            if precipitation:
                output += ' Rain: {} mm.'.format(point.precipitation)
            output += '\n'
        tot_avg = tot_avg/ len(points)
        output += 'Average: {:.2f}.\n'.format(tot_avg)
        return output

    def str_avgs(self, date):
        output = self.TOP_REPR_FMT.format(location=self.location, date=date.isoformat())
        avgs, tot_avg  = self.calculate_avg(date)
        outputs = ['{:.2f} deg celsius.'.format(avg) if avg else "No data" for avg in avgs]
        output += self.AVGS_FMT.format(*outputs)
        output += 'Total: {:.2f} deg celsius.\n'.format(tot_avg)
        return output

    def calculate_avg(self, date):
        # Calculate averages for times 0-8, 8-12, 12-6 and 6-0
        # and return them as a list of avgs or None values if empty, along with the total avg
        points = self.timepoints[date]
        vals = [[] for _ in range(len(self.AVG_RANGES))]
        avgs = [None for _ in range(len(self.AVG_RANGES))]
        tot_avg = 0
        for point in points:
            hour = point.time.hour
            for i in range(len(self.AVG_RANGES)):
                if hour >= self.AVG_RANGES[i][0] and hour <= self.AVG_RANGES[i][1]:
                    tot_avg += point.temperature()
                    vals[i].append(point.temperature())
        for i, val in enumerate(vals):
            # Dont divide by 0
            if len(val) > 0:
                avgs[i] = sum(val) / len(val)
        return avgs, tot_avg / len(points)

    def print_days(self, days, precipitation=False, averages=False):
        today = datetime.date.today()
        curdate = today
        for day in range(days):
            curdate = today + datetime.timedelta(days=day)
            if curdate in self.timepoints:
                if averages:
                    print(self.str_avgs(curdate))
                else:
                    print(self.str_timepoints_date(curdate, precipitation))
            else:
                print("No data for date: {}".format(curdate.isoformat()))

    def __repr__(self):
        # Print out the entire timeseries
        output = ''
        for date in sorted(self.timepoints.keys()):
            output += self.str_timepoints_date(date) + '\n'
        return output
