class LoadCities:
    """
    Loads cities and corresponding coordinates from a text-file
    and stores them in a dict.
    """

    def __init__(self, filename='cities.txt'):
        self.cities = dict()
        self._load_file(filename)

    def _load_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                # Ignore comments
                if line[0] == '#':
                    continue
                self._parse_line(line)

    def _parse_line(self, line):
        line = line.split()
        name = line[0]
        coord = (float(line[1]), float(line[2]))
        self.cities[name] = coord

    def get_cities(self):
        return self.cities