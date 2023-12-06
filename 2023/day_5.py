import re
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Range:
    dst_range_start: int
    src_range_start: int
    range_len: int

    @property
    def src_range_end(self) -> int:
        return self.src_range_start + self.range_len - 1

    @property
    def dst_range_end(self) -> int:
        return self.dst_range_start + self.range_len - 1


@dataclass
class Map:
    ranges: List[Range] = field(default_factory=list)

    def convert(self, number: int) -> int:
        for r in self.ranges:
            if r.src_range_start <= number <= r.src_range_end:
                return r.dst_range_start + (number - r.src_range_start)
        return number

    def convert_range(self, input_range: Tuple[int, int]):
        if input_range[1] < input_range[0]:
            return
        matched = False
        for r in self.ranges:
            if r.src_range_start <= input_range[0] and input_range[1] <= r.src_range_end:
                matched = True
                yield tuple(
                    [
                        r.dst_range_start + (input_range[0] - r.src_range_start),
                        r.dst_range_start + (input_range[1] - r.src_range_start),
                    ]
                )

            elif r.src_range_start <= input_range[0] < r.src_range_end < input_range[1]:
                matched = True
                yield tuple([r.dst_range_start + (input_range[0] - r.src_range_start), r.dst_range_end])
                self.convert_range(tuple((r.src_range_end + 1, input_range[1])))

            elif input_range[0] < r.src_range_start < input_range[1] <= r.src_range_end:
                matched = True
                self.convert_range(tuple((input_range[0], r.src_range_start - 1)))
                yield tuple([r.dst_range_start, r.dst_range_start + (input_range[1] - r.src_range_start)])

            elif input_range[0] < r.src_range_start and r.src_range_end < input_range[1]:
                matched = True
                self.convert_range(tuple((input_range[0], r.src_range_start - 1)))
                yield tuple([r.dst_range_start, r.dst_range_end])
                self.convert_range(tuple((r.src_range_end + 1, input_range[1])))

        if not matched:
            yield input_range


def main():
    with open("day_5_input.txt") as f:
        for line in f.readlines():
            if re.match(r"^seeds:", line):
                numbers = [int(i) for i in re.findall(r"\d+", line)]
                seeds_part_one = numbers
                seeds_part_two = list()
                for i in range(0, len(numbers), 2):
                    seeds_part_two.append((numbers[i], numbers[i] + numbers[i + 1] - 1))  # Both numbers included
            elif line.startswith("seed-to-soil"):
                seed_to_soil = Map()
                current_map = seed_to_soil
            elif line.startswith("soil-to-fertilizer"):
                soil_to_fertilizer = Map()
                current_map = soil_to_fertilizer
            elif line.startswith("fertilizer-to-water"):
                fertilizer_to_water = Map()
                current_map = fertilizer_to_water
            elif line.startswith("water-to-light"):
                water_to_light = Map()
                current_map = water_to_light
            elif line.startswith("light-to-temperature"):
                light_to_temperature = Map()
                current_map = light_to_temperature
            elif line.startswith("temperature-to-humidity"):
                temperature_to_humidity = Map()
                current_map = temperature_to_humidity
            elif line.startswith("humidity-to-location"):
                humidity_to_location = Map()
                current_map = humidity_to_location
            elif len(line.strip()) == 0:
                continue
            else:
                numbers = [int(i) for i in re.findall(r"\d+", line)]
                current_map.ranges.append(Range(numbers[0], numbers[1], numbers[2]))

    lowest_location = None
    for seed in seeds_part_one:
        location = humidity_to_location.convert(
            temperature_to_humidity.convert(
                light_to_temperature.convert(
                    water_to_light.convert(
                        fertilizer_to_water.convert(soil_to_fertilizer.convert(seed_to_soil.convert(seed)))
                    )
                )
            )
        )
        if lowest_location is None or location < lowest_location:
            lowest_location = location
    print(f"Part 1: {lowest_location}")

    lowest_location = None
    for r in seeds_part_two:
        for a in seed_to_soil.convert_range(r):
            for b in soil_to_fertilizer.convert_range(a):
                for c in fertilizer_to_water.convert_range(b):
                    for d in water_to_light.convert_range(c):
                        for e in light_to_temperature.convert_range(d):
                            for f in temperature_to_humidity.convert_range(e):
                                for g in humidity_to_location.convert_range(f):
                                    if lowest_location is None or g[0] < lowest_location:
                                        lowest_location = g[0]
    print(f"Part 2: {lowest_location}")


if __name__ == "__main__":
    main()
