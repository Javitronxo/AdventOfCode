# NOTE: Drunk coding, way past my Ballmer Peak (https://xkcd.com/323/)
from typing import Dict, List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.connections = list()

    @property
    def small_cave(self) -> bool:
        return self.name.islower()


def get_paths(tree: Dict[str, Node], part_one: bool = True) -> List[List[Node]]:
    start_node = tree["start"]
    end_node = tree["end"]
    queue = [[start_node]]
    paths = list()
    while queue:
        nodes = queue.pop()
        last_node = nodes[-1]
        disallow_small_cave = any(node.small_cave and nodes.count(node) > 1 for node in nodes)
        for connection in last_node.connections:
            if (
                connection == start_node
                or (part_one and connection.small_cave and connection in nodes)
                or (not part_one and connection in nodes and connection.small_cave and disallow_small_cave)
            ):
                continue
            elif connection == end_node:
                paths.append(nodes + [connection])
            else:
                queue.append(nodes + [connection])
    return paths


def main():
    nodes = dict()
    with open("day_12_input.txt") as f:
        for line in f.readlines():
            start, end = line.strip().split("-")
            if start not in nodes:
                nodes[start] = Node(start)
            if end not in nodes:
                nodes[end] = Node(end)
            nodes[start].connections.append(nodes[end])
            nodes[end].connections.append(nodes[start])

    print(f"Part 1: {len(get_paths(nodes, part_one=True))}")
    print(f"Part 1: {len(get_paths(nodes, part_one=False))}")


if __name__ == "__main__":
    main()
