def main():
    groups = list()
    with open("day_6_input.txt") as f:
        answers = list()
        for line in f.readlines():
            if line.strip():
                answers.append(line.strip())
            else:
                groups.append(answers)
                answers = list()
        if answers:
            groups.append(answers)

    part_1 = 0
    part_2 = 0
    for group in groups:
        part_1 += len(set("".join(group)))
        answer = set(group[0])
        for i in range(1, len(group)):
            answer = answer.intersection(set(group[i]))
        part_2 += len(answer)

    print(f"Part 1: The number of positive answers is {part_1}")
    print(f"Part 2: The number of positive answers is {part_2}")


if __name__ == "__main__":
    main()
