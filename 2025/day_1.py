def main():
    dial = 50
    password_1 = 0
    password_2 = 0

    with open("day_1_input.txt") as f:
        for line in f.readlines():
            direction = line[0]
            turns = int(line[1:])

            if turns >= 100:
                password_2 += turns // 100
                turns %= 100

            if direction == "R":
                new_dial = dial + turns
                if new_dial > 100:
                    password_2 += 1
            else:
                new_dial = dial - turns
                if dial != 0 and new_dial < 0:
                    password_2 += 1

            dial = new_dial % 100
            if dial == 0:
                password_1 += 1
                password_2 += 1

    print(f"Part 1: {password_1}")
    print(f"Part 2: {password_2}")


if __name__ == "__main__":
    main()
