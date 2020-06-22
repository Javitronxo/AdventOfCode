import re
from collections import defaultdict


class Reindeer:
    def __init__(self, name: str, speed: int, fly_time: int, rest_time: int):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.current_position = 0

    def get_position(self, time: int) -> int:
        interval_time = self.fly_time + self.rest_time
        intervals = time // interval_time
        remainder = time % interval_time
        distance = (self.speed * self.fly_time * intervals) + (min(remainder, self.fly_time) * self.speed)
        self.current_position = distance
        return distance


def main():
    race_time = 2503
    line_pattern = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

    reindeers = list()
    with open('day_14_input.txt') as f_in:
        for line in f_in.readlines():
            reindeer_name, speed, fly_time, rest_time = re.findall(line_pattern, line)[0]
            reindeer = Reindeer(reindeer_name, int(speed), int(fly_time), int(rest_time))
            reindeers.append(reindeer)

    # Part 1
    max_distance = (None, -1)
    for reindeer in reindeers:
        distance = reindeer.get_position(race_time)
        if distance > max_distance[1]:
            max_distance = (reindeer.name, distance)
    print('%s got the most distance with %d km' % (max_distance[0], max_distance[1]))

    # Part 2
    scorecard = defaultdict(int)
    for seconds in range(1, race_time + 1):
        max_distance = -1
        for reindeer in reindeers:
            distance = reindeer.get_position(seconds)
            if distance > max_distance:
                max_distance = distance
        for reindeer_name in [reindeer.name for reindeer in reindeers if reindeer.current_position == max_distance]:
            scorecard[reindeer_name] += 1
    print('The winning reindeer has %d points' % max(list(scorecard.values())))


if __name__ == '__main__':
    main()
