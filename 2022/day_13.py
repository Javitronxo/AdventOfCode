from copy import deepcopy
from typing import List, Optional


def compare(left: List, right: List) -> Optional[bool]:
    while len(left) > 0:
        leftmost = left.pop(0)
        try:
            rightmost = right.pop(0)
        except IndexError:
            return False
        if isinstance(leftmost, int) and isinstance(rightmost, int):
            if leftmost < rightmost:
                return True
            elif leftmost > rightmost:
                return False
            else:
                continue
        elif isinstance(leftmost, int) and (ret := compare([leftmost], rightmost)) is not None:
            return ret
        elif isinstance(rightmost, int) and (ret := compare(leftmost, [rightmost])) is not None:
            return ret
        elif isinstance(rightmost, list) and (ret := compare(leftmost, rightmost)) is not None:
            return ret
        else:
            continue
    return True if len(right) > 0 else None


def main():
    pair_count = 0
    part_one = list()
    all_packets = list()

    with open("day13_input.txt") as f:
        pair = list()
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            pair.append(eval(line.strip()))
            all_packets.append(eval(line.strip()))
            if len(pair) == 2:
                pair_count += 1
                if compare(pair[0], pair[1]):
                    part_one.append(pair_count)
                pair = list()

    print(f"Part 1: {sum(part_one)}")

    indices = [1, 2]
    for packet in all_packets:
        if compare(deepcopy(packet), [[6]]):
            indices[1] += 1
            if compare(deepcopy(packet), [[2]]):
                indices[0] += 1
    print(f"Part 2: {indices[0] * indices[1]}")


if __name__ == "__main__":
    main()
