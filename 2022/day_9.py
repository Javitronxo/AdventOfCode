from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(f"{self.x},{self.y}")

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def follow(self, other: Point) -> Point:
        diff_x = other.x - self.x
        diff_y = other.y - self.y
        if abs(diff_x) < 2 and abs(diff_y) < 2:
            return self
        elif abs(diff_x) == abs(diff_y):
            return Point(other.x - int(diff_x / abs(diff_x)), other.y - int(diff_y / abs(diff_y)))
        elif abs(diff_x) > abs(diff_y):
            return Point(other.x - int(diff_x / abs(diff_x)), other.y)
        else:
            return Point(other.x, other.y - int(diff_y / abs(diff_y)))


def simulate(moves: List[Tuple[str, int]], rope_len: int) -> Set[Point]:
    visited_squares = set()
    rope = [Point(0, 0) for _ in range(rope_len)]
    visited_squares.add(Point(0, 0))
    vectors = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}
    for move in moves:
        for _ in range(move[1]):
            for knot in range(len(rope)):
                if knot == 0:
                    rope[knot] += vectors[move[0]]
                else:
                    rope[knot] = rope[knot].follow(rope[knot - 1])
            visited_squares.add(rope[-1])
    return visited_squares


def main():
    moves = list()
    with open("day_9_input.txt") as f:
        for line in f.readlines():
            direction, steps = line.split()
            moves.append((direction, int(steps)))

    print(f"Part 1: {len(simulate(moves, rope_len=2))}")
    print(f"Part 2: {len(simulate(moves, rope_len=10))}")


if __name__ == "__main__":
    main()
