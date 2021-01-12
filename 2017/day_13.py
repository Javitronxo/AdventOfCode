from dataclasses import dataclass
from itertools import count


@dataclass
class Layer:
    depth: int
    range: int
    scanner: int = 0
    move_down: bool = False

    @property
    def severity(self):
        return self.depth * self.range

    def next(self):
        if self.scanner in [0, self.range - 1]:
            self.move_down = not self.move_down
        self.scanner += 1 if self.move_down else -1


def main():
    firewall = list()
    with open("day_13_input.txt") as f:
        for line in f.read().splitlines():
            parts = line.split(": ")
            layer = Layer(int(parts[0]), int(parts[1]))
            firewall.append(layer)

    firewall_depth = firewall[-1].depth + 1
    severity = 0
    for step in range(firewall_depth):
        try:
            layer = [layer for layer in firewall if layer.depth == step][0]
            if layer.scanner == 0:
                severity += layer.severity
        except IndexError:
            pass
        [layer.next() for layer in firewall]
    print(f"Part 1: {severity}")

    for delay in count():
        busted = False
        for layer in firewall:
            if (layer.depth + delay) % (2 * layer.range - 2) == 0:
                busted = True
                break
        if not busted:
            break
        delay += 1
    print(f"Part 2: {delay}")


if __name__ == "__main__":
    main()
