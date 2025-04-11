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
            for line in f.readline():
                # Ignore comments
                if line[0] == '#':
                    continue
                name, coords = self._parse_line(line)
                self.cities[name] = coords

    def _parse_line(self, line):
        line = line.split()
        name = line[0]
        coords = (line[1], line[2])

    def get_cities(self):
        return self.cities