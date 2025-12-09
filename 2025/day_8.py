import math


def get_distance(box_1, box_2):
    return math.sqrt((box_1[0] - box_2[0]) ** 2 + (box_1[1] - box_2[1]) ** 2 + (box_1[2] - box_2[2]) ** 2)


def main():
    boxes = []
    n_paths = 10
    with open("day_8_test.txt") as f:
        for line in f.readlines():
            parts = line.strip().split(",")
            boxes.append(tuple(map(int, parts)))

    boxes_by_distance = {}
    for i, box_1 in enumerate(boxes):
        for j, box_2 in enumerate(boxes):
            if i == j:
                continue
            distance = get_distance(box_1, box_2)
            boxes_by_distance[distance] = (i, j)

    circuits = [{i} for i in range(len(boxes))]
    circuit_indices_by_box = {i: i for i in range(len(boxes))}
    circuit_count = len(circuits)

    sorted_distances = sorted(boxes_by_distance.keys())
    box_1, box_2 = None, None
    for count, distance in enumerate(sorted_distances):
        box_1, box_2 = boxes_by_distance[distance]

        circuit_1 = circuit_indices_by_box[box_1]
        circuit_2 = circuit_indices_by_box[box_2]
        if circuit_1 != circuit_2:
            circuits[circuit_1].update(circuits[circuit_2])
            for node in circuits[circuit_2]:
                circuit_indices_by_box[node] = circuit_1
            circuits[circuit_2] = {}
            circuit_count -= 1

        count += 1
        if count == n_paths:
            print(f"Part 1: {math.prod(sorted([len(c) for c in circuits if c])[-3:])}")
        if circuit_count == 1:
            break

    part_2 = boxes[box_1][0] * boxes[box_2][0]
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
