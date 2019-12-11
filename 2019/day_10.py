# https://adventofcode.com/2019/day/10
import sys
from math import copysign


def read_input_file(file_name):
    input_map = list()
    with open(file_name) as f_in:
        for line in f_in.readlines():
            input_map.append(line.strip())
    return input_map


class Asteroid:
    """
    Represent an asteroid by moving the cartesian space to something that I can visualize without a headache:
    - Pass a reference point to use as origin of coordinates
    - Flip the Y-axis
    """
    def __init__(self, x, y, ref):
        self.x_rel = (x - ref[0])
        self.y_rel = -(y - ref[1])
        self.x_abs = x
        self.y_abs = y
        self.quarter = self.get_quarter()
        self.distance = abs(self.x_rel + self.y_rel)  # Manhattan distance to reference point
        self.slope = self.get_slope()

    def get_quarter(self):
        if self.x_rel >= 0:
            return 0 if self.y_rel >= 0 else 1
        else:
            return 2 if self.y_rel < 0 else 3

    def get_slope(self):
        try:
            return abs(self.y_rel / self.x_rel)
        except ZeroDivisionError:
            return sys.maxsize


class AsteroidMap:
    def __init__(self, input_map):
        self.input_map = input_map
        self.width = len(self.input_map[0])
        self.length = len(self.input_map)
        self.asteroids = self.get_asteroids()

    def get_asteroids(self):
        asteroids = list()
        for y in range(self.length):
            for x in range(self.width):
                if self.input_map[y][x] == '#':
                    asteroids.append((x, y))
        return asteroids

    def get_best_asteroid(self):
        max_visible_asteroids = list()
        best_asteroid = None
        for asteroid in self.asteroids:
            visible_asteroids = self.count_visible_asteroids(asteroid)
            if len(visible_asteroids) > len(max_visible_asteroids):
                best_asteroid = asteroid
                max_visible_asteroids = visible_asteroids
        return max_visible_asteroids, best_asteroid

    def count_visible_asteroids(self, asteroid_ref):
        all_other_asteroids = self.asteroids[:]
        all_other_asteroids.remove(asteroid_ref)
        remaining_visible_asteroids = all_other_asteroids[:]

        x_0, y_0 = asteroid_ref[0], asteroid_ref[1]
        for asteroid in all_other_asteroids:
            x_1, y_1 = asteroid[0], asteroid[1]
            x_diff, y_diff = x_1 - x_0, y_1 - y_0
            increment = 1
            # Remove the vertical asteroids
            if x_diff == 0:
                while 0 <= y_1 + copysign(increment, y_diff) < self.length:
                    asteroid_to_remove = (x_0, y_1 + copysign(increment, y_diff))
                    self.remove_asteroid(asteroid_to_remove, remaining_visible_asteroids)
                    increment += 1
            # Remove the horizontal asteroids
            elif y_diff == 0:
                while 0 <= x_1 + copysign(increment, x_diff) < self.width:
                    asteroid_to_remove = (x_1 + copysign(increment, x_diff), y_0)
                    self.remove_asteroid(asteroid_to_remove, remaining_visible_asteroids)
                    increment += 1
            # Remove the diagonal asteroids
            elif abs(x_diff) == abs(y_diff):
                while 0 <= (x_1 + copysign(increment, x_diff)) < self.width and \
                        0 <= (y_1 + copysign(increment, y_diff)) < self.length:
                    asteroid_to_remove = (x_1 + copysign(increment, x_diff), y_1 + copysign(increment, y_diff))
                    self.remove_asteroid(asteroid_to_remove, remaining_visible_asteroids)
                    increment += 1
            # Remove those in any other angle
            else:
                slope = y_diff / x_diff
                increment_y = 1
                while 0 <= y_1 + copysign(increment_y, y_diff) < self.length:
                    increment_x = 1
                    while 0 <= x_1 + copysign(increment_x, x_diff) < self.width:
                        asteroid_to_remove = (x_1 + copysign(increment_x, x_diff), y_1 + copysign(increment_y, y_diff))
                        if asteroid_to_remove[1] - y_0 == slope * (asteroid_to_remove[0] - x_0):
                            self.remove_asteroid(asteroid_to_remove, remaining_visible_asteroids)
                        increment_x += 1
                    increment_y += 1

        return remaining_visible_asteroids

    @staticmethod
    def remove_asteroid(asteroid, remaining_visible_asteroids):
        try:
            remaining_visible_asteroids.remove(asteroid)
        except ValueError:
            pass

    def vaporize_asteroids(self, battle_station):
        asteroids_vaporized = list()
        asteroids_to_vaporize = [Asteroid(x, y, battle_station) for x, y in self.asteroids if (x, y) != battle_station]

        quarter = 0
        while len(asteroids_to_vaporize):
            last_slope = None
            asteroids_to_vaporize.sort(key=lambda x: x.distance, reverse=False)
            if quarter in [0, 2]:
                asteroids_to_vaporize.sort(key=lambda x: x.slope, reverse=True)
            else:
                asteroids_to_vaporize.sort(key=lambda x: x.slope, reverse=False)

            asteroids_vaporized_cache = list()
            for asteroid in asteroids_to_vaporize:
                if asteroid.quarter != quarter or asteroid.slope == last_slope:
                    continue
                asteroids_vaporized.append((asteroid.x_abs, asteroid.y_abs))
                asteroids_vaporized_cache.append(asteroid)
                last_slope = asteroid.slope

            for asteroid in asteroids_vaporized_cache:
                asteroids_to_vaporize.remove(asteroid)
            quarter = (quarter + 1) % 4

        return asteroids_vaporized


def main():
    input_map = read_input_file('day_10_input.txt')
    asteroid_map = AsteroidMap(input_map)

    max_visible_asteroids, best_asteroid = asteroid_map.get_best_asteroid()
    result_first_part = len(max_visible_asteroids)
    print("First part result: {}".format(result_first_part))  # 227

    asteroids_vaporized = asteroid_map.vaporize_asteroids(best_asteroid)
    result_second_part = asteroids_vaporized[200 - 1][0] * 100 + asteroids_vaporized[200 - 1][1]
    print("Second part result: {}".format(result_second_part))  # 604


if __name__ == '__main__':
    main()
