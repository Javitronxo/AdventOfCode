import re

from lib.utils import lcm


class Node:
    def __init__(self, input_line: str):
        parts = re.findall(r"(\w+) = \((\w+), (\w+)\)", input_line)
        self.name = parts[0][0]
        self.left = parts[0][1]
        self.right = parts[0][2]


def main():
    # Parse input file
    nodes = dict()
    with open("day_8_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                instructions = line.strip()
            elif i == 1:
                continue
            else:
                node = Node(line)
                nodes[node.name] = node

    # Logic for part 1
    current_node = nodes["AAA"]
    steps = 0
    while current_node.name != "ZZZ":
        if instructions[steps % len(instructions)] == "R":
            current_node = nodes[current_node.right]
        else:
            current_node = nodes[current_node.left]
        steps += 1
        if current_node.name == "ZZZ":
            break
    print(f"Part 1: {steps}")

    # Logic for part 2
    steps_to_z = list()
    steps = 0
    for node in [node for node in nodes.values() if node.name.endswith("A")]:
        while not node.name.endswith("Z"):
            if instructions[steps % len(instructions)] == "R":
                node = nodes[node.right]
            else:
                node = nodes[node.left]
            steps += 1
            if node.name.endswith("Z"):
                steps_to_z.append(steps)
                break
    print(f"Part 2: {lcm(steps_to_z)}")


if __name__ == "__main__":
    main()
