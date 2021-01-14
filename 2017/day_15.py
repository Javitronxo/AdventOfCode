import re
from dataclasses import dataclass


@dataclass
class Generator:
    factor: int
    value: int
    orig_value: int
    multiple: int

    def reset(self):
        self.value = self.orig_value

    def next_value(self, part_two: bool = False) -> str:
        self.value = (self.value * self.factor) % 2147483647
        bin_value = bin(self.value)[2:].zfill(16)
        if not part_two or (part_two and bin_value[-self.multiple :] == "0" * self.multiple):
            return bin_value[-16:]
        else:
            return self.next_value(part_two=True)


def main():
    factors = {"A": 16807, "B": 48271}
    multiples_mask = {"A": 2, "B": 3}

    generators = dict()
    with open("day_15_input.txt") as f:
        for line in f.read().splitlines():
            letter, start = re.search(r"Generator (\w) starts with (\d+)", line).groups()
            generators[letter] = Generator(factors[letter], int(start), int(start), multiples_mask[letter])

    n_pairs = 40_000_000
    final_count = sum(1 for _ in range(n_pairs) if generators["A"].next_value() == generators["B"].next_value())
    print(f"Part 1: {final_count}")

    [generator.reset() for generator in generators.values()]
    n_pairs = 5_000_000
    final_count = sum(1 for _ in range(n_pairs) if generators["A"].next_value(True) == generators["B"].next_value(True))
    print(f"Part 2: {final_count}")


if __name__ == "__main__":
    main()
