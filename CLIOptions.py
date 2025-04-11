import sys
import re
import logging

from getopt import getopt

class CLIOptions:
    LOGGER = logging.getLogger(__name__)
    # Options for getopt cli flags
    SHORT_OPTIONS = 'c:n:h'
    HELP_TEXT = '''
usage: python fetchweather.py [options]  
    options:
        -c      lat,lon  - Provide weather data for the given coordinates.
        -n      cityname - Provide weather data for the given city, if the coords exist in cities.txt
        -h               - Presents this text
    If both coord and city are given, the program will only show the data for the coord.
    If no options are given the program will default to showing data for Oslo 
    for the following day.
'''
    DEFAULT_CITY = 'oslo'
    # Regex to match coordinates like 39.2,20 and capture them
    COORD_REGEX = re.compile(r'(\d+(?:.?\d+)),(\d+(?:.?\d+))')
    # Coords < -180 or > 180 are nonsense
    MIN_COORD_VAL = -180
    MAX_COORD_VAL = 180

    def __init__(self, argv):
        self.city = None
        self.coord = None
        # First arg is program name, so ignore it
        self.parse_opts(argv[1:])
        # Default option if none are provided
        if not self.city and not self.coord:
            self.city = CLIOptions.DEFAULT_CITY

    def parse_opts(self, args):
        try:
            opts, extra = getopt(args, CLIOptions.SHORT_OPTIONS)
        except getopt.GetoptError as err:
            CLIOptions.LOGGER.error(str(err))
            print(CLIOptions.HELP_TEXT)
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-c':
                self.coord = self.parse_coord(arg)
            elif opt == '-n':
                self.city = arg
            elif opt == '-h':
                print(CLIOptions.HELP_TEXT)
                sys.exit(0)
        
    def parse_coord(self, coords):
        m = CLIOptions.COORD_REGEX.match(coords)
        try:
            if not m or len(m.groups()) != 2:
                # We're looking for lat and lon separated by a comma
                raise ValueError("Invalid coord format.")

            coord = (float(m.groups()[0]), float(m.groups()[1]))

            # If the values are off we throw an error here, not later
            for val in coord:
                if val < CLIOptions.MIN_COORD_VAL or val > CLIOptions.MAX_COORD_VAL:
                    raise ValueError("Coord must be in the range {} - {}".format(CLIOptions.MIN_COORD_VAL, CLIOptions.MAX_COORD_VAL))    
            return coord
        except ValueError as e:
            CLIOptions.LOGGER.error('Coords not in the right format: {}'.format(e.reason))
            sys.exit(1)
