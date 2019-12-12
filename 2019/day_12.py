# https://adventofcode.com/2019/day/12
import re
from copy import deepcopy
from itertools import combinations
from math import gcd


def read_input_file(file_name):
    input_pattern = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
    moons = list()
    with open(file_name) as f:
        for line in f.readlines():
            x, y, z = re.match(input_pattern, line).groups()
            moon = Moon(x, y, z)
            moons.append(moon)
    return moons


class System:
    def __init__(self, moons):
        self.moons = moons[:]
        self.cycles = [None, None, None]

    def get_total_energy(self):
        total_energy = 0
        for moon in self.moons:
            total_energy += moon.get_total_energy()
        return total_energy

    def evolve(self, time_step=1):
        for t in range(1, time_step + 1):
            for combination in combinations(self.moons, 2):
                moon_1, moon_2 = combination
                moon_1.apply_gravity(moon_2)
                moon_2.apply_gravity(moon_1)

            for i in range(len(self.moons)):
                self.moons[i].apply_velocity()

            for i in range(len(self.cycles)):
                if self.cycles[i]:
                    continue
                if all([moon.position[i] == moon.initial_state[0][i] and moon.velocity[i] == moon.initial_state[1][i]
                        for moon in self.moons]):
                    self.cycles[i] = t
            if all(self.cycles):
                return self.get_planetary_alignment(self.cycles)

    @staticmethod
    def get_planetary_alignment(cycle_values):
        lcm = cycle_values[0]
        for i in cycle_values[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm


class Moon:
    def __init__(self, x, y, z):
        self.position = [int(x), int(y), int(z)]
        self.velocity = [0, 0, 0]
        self.initial_state = (self.position[:], self.velocity[:])

    def apply_velocity(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

    def apply_gravity(self, moon):
        for i in range(len(self.position)):
            if self.position[i] > moon.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < moon.position[i]:
                self.velocity[i] += 1

    def get_potential_energy(self):
        return sum(map(abs, self.position))

    def get_kinetic_energy(self):
        return sum(map(abs, self.velocity))

    def get_total_energy(self):
        return self.get_kinetic_energy() * self.get_potential_energy()


def main():
    moons = read_input_file('day_12_input.txt')

    system = System(deepcopy(moons))
    system.evolve(1000)
    result_first_part = system.get_total_energy()
    print("First part result: {}".format(result_first_part))

    # https://en.wikipedia.org/wiki/Least_common_multiple#Planetary_alignment
    system = System(deepcopy(moons))
    result_second_part = system.evolve(10000000000)
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
