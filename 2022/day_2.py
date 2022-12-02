def get_points_part_one(cpu, me) -> int:
    points_matrix = {
        "A": {"X": 4, "Y": 8, "Z": 3},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 7, "Y": 2, "Z": 6},
    }
    return points_matrix[cpu][me]


def get_points_part_two(cpu, me) -> int:
    points_matrix = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7},
    }
    return points_matrix[cpu][me]


def main():
    part_one_score = 0
    part_two_score = 0
    with open("day_2_input.txt") as f:
        for line in f.readlines():
            (cpu, me) = line.split()
            part_one_score += get_points_part_one(cpu, me)
            part_two_score += get_points_part_two(cpu, me)
    print(f"Part 1: {part_one_score}")
    print(f"Part 2: {part_two_score}")


if __name__ == "__main__":
    main()
