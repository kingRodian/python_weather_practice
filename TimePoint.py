class TimePoint:
    """
    Holds a datetime and datapoints relating to the weather at that time.
    """

    REPR_FORMAT = '{time} - {temp:>5} deg celsius.'

    def __init__(self, time, precipitation, air_pressure_at_sea_level, air_temperature,
     cloud_area_fraction, relative_humidity, wind_from_direction, wind_speed):
        self.time = time
        self.air_pressure = air_pressure_at_sea_level
        self.air_temperature = air_temperature
        self.cloud_area = cloud_area_fraction
        self.relative_humidity = relative_humidity
        self.wind_from_direction = wind_from_direction
        self.wind_speed = wind_speed
        self.precipitation = precipitation


    def time(self):
        return self.time

    def temperature(self):
        return self.air_temperature
    
    def humidity(self):
        return self.relative_humidity

    def wind(self):
        return self.wind_speed

    def __repr__(self):
        isotime = self.time.time().isoformat(timespec="minutes")
        return self.REPR_FORMAT.format(time=isotime, temp=self.temperature())

    # Sorting methods to compare timepoints
    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __eq__(self, other):
        return self.time == other.time

    def __hash__(self):
        return hash(self.time)