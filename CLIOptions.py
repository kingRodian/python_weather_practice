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
    If no options are given the program will default to showing data for Oslo 
    for the following day.
'''
    DEFAULT_CITY = 'oslo'
    # Regex to match coordinates like 39.2,20 and capture them
    COORD_REGEX = re.compile('(\d+(?:.?\d+)),(\d+(?:.?\d+))')

    def __init__(self, argv):
        self.city = CLIOptions.DEFAULT_CITY
        self.coord = None
        # First arg is program name, so ignore it
        self.parse_opts(argv[1:])

    def parse_opts(self, args):
        try:
            opts, extra = getopt(args, CLIOptions.SHORT_OPTIONS)

        except getopt.GetoptError as err:
            CLIOptions.LOGGER.error(str(err))
            print(CLIOptions.HELP_TEXT)
            sys.exit(2)

        for opt, arg in options:
            if opt == '-c':
                self.coord = self.parse_coord(arg)
            if opt == '-n':
                self.city = arg
            elif opt == '-h':
                print(CLIOptions.HELP_TEXT)
                sys.exit(0)
        

    def parse_coord(self, coords):
        m = CLIOptions.COORD_REGEX.match(coords)
        if not m:
            return
        try:
            self.coord = (float(m.groups()[0]), float(m.groups()[1]))
        except ValueError as e:
            CLIOptions.LOGGER.error('Coords not in the right format: {}'.format(e.reason))
            sys.exit(1)
