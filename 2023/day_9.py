def main():
    part_one_values = list()
    part_two_values = list()
    with open("day_9_input.txt") as f:
        for line in f.readlines():
            history = [int(i) for i in line.strip().split()]
            new_history = [history[i] - history[i - 1] for i in range(1, len(history))]
            process = [history, new_history]
            while set(new_history) != {0}:
                new_history = [new_history[i] - new_history[i - 1] for i in range(1, len(new_history))]
                process.append(new_history)

            process[-1].append(0)
            process[-1].insert(0, 0)
            for i in range(len(process) - 2, -1, -1):
                process[i].append(process[i][-1] + process[i + 1][-1])
                process[i].insert(0, process[i][0] - process[i + 1][0])
            part_one_values.append(process[0][-1])
            part_two_values.append(process[0][0])

    print(f"Part 1: {sum(part_one_values)}")
    print(f"Part 2: {sum(part_two_values)}")


if __name__ == "__main__":
    main()
