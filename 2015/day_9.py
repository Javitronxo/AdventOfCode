import re
from itertools import permutations


class City:
    def __init__(self, name: str):
        self.name = name
        self.destinations = dict()

    def add_destination(self, destination: str, distance: int):
        self.destinations[destination] = distance


def main():
    line_pattern = r'(\w+) to (\w+) = (\d+)'
    all_cities = list()
    with open('day_9_input.txt') as f_in:
        for line in f_in.readlines():
            line = line.strip()
            origin, destination, distance = re.findall(line_pattern, line)[0]
            for origin, destination in permutations([origin, destination]):
                if origin not in [node.name for node in all_cities]:
                    city = City(origin)
                    all_cities.append(city)
                else:
                    city = [node for node in all_cities if node.name == origin][0]
                city.add_destination(destination, int(distance))

    all_distances = list()
    for cities in permutations(all_cities):
        try:
            distance = 0
            for i in range(len(cities) - 1):
                distance += cities[i].destinations[cities[i + 1].name]
            all_distances.append(distance)
        except KeyError:
            print('ERROR: There is no path like %r' % [city.name for city in cities])
    print('Minimum distance is %d' % min(all_distances))
    print('Maximum distance is %d' % max(all_distances))


if __name__ == '__main__':
    main()