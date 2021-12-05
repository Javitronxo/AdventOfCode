def main():
    position = [0, 0]
    with open("day_2_input.txt") as f:
        for line in f.readlines():
            cmd, unit = line.split()
            if cmd == "forward":
                position[0] += int(unit)
            elif cmd == "down":
                position[1] += int(unit)
            elif cmd == "up":
                position[1] -= int(unit)
    print(f"Part 1: {position[0] * position[1]}")

    position = [0, 0]
    aim = 0
    with open("day_2_input.txt") as f:
        for line in f.readlines():
            cmd, unit = line.split()
            if cmd == "forward":
                position[0] += int(unit)
                position[1] += aim * int(unit)
            elif cmd == "down":
                aim += int(unit)
            elif cmd == "up":
                aim -= int(unit)
    print(f"Part 2: {position[0] * position[1]}")


if __name__ == "__main__":
    main()
