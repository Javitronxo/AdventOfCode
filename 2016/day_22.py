import re
from dataclasses import dataclass
from typing import List, Tuple

Point = Tuple[int, int]


@dataclass
class Node:
    coordinates: Point
    size: int
    used: int
    available: int
    use_pct: int


def get_viable_pairs(nodes: List[Node]) -> List[Tuple[Node, Node]]:
    viable_pairs = list()
    for i, node_a in enumerate(nodes):
        for j, node_b in enumerate(nodes):
            if i == j:
                continue
            elif 0 < node_a.used < node_b.available:
                viable_pairs.append((node_a, node_b))
    return viable_pairs


def main():
    line_pattern = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"
    nodes = list()
    with open("day_22_input.txt") as f:
        for line in f.read().splitlines():
            if not line.startswith("/dev"):
                continue
            x, y, size, used, available, use_pct = re.search(line_pattern, line).groups()
            nodes.append(Node((int(x), int(y)), int(size), int(used), int(available), int(use_pct)))

    print(f"Part 1: {len(get_viable_pairs(nodes))}")

    # Print the node grid to solve part 2
    grid_dim = (max(node.coordinates[0] for node in nodes), max(node.coordinates[1] for node in nodes))
    for x in range(grid_dim[0] + 1):
        line = str()
        for y in range(grid_dim[1] + 1):
            node = [node for node in nodes if node.coordinates == (x, y)][0]
            if node.coordinates == (0, 0):
                line += "(.)"
            elif node.coordinates == (grid_dim[0], 0):
                line += "G"
            elif node.use_pct == 0:
                line += "_"
            elif node.use_pct > 90:
                line += "#"
            else:
                line += "."
            line += "\t"
        print(line)

    # To solve part 2:
    # 1) Count the minimum number of steps to move the empty node to between the origin and destination
    # 2) Move the empty node adjacent to the goal node and swap them
    # 3) Count the number of times we have to repeat the swap between goal and empty until we reach the origin
    # In my particular case: 26 + 22 + (5 * 28)
    #                        1)   2)   3)


if __name__ == "__main__":
    main()
