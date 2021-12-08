def main():
    part_one = 0
    with open("day_8_input.txt") as f:
        for line in f.readlines():
            _, right = line.split(" | ")
            for number in right.split():
                if len(number) in [2, 3, 4, 7]:
                    part_one += 1
    print(f"Part 1: {part_one}")

    # Visual to build the heuristics for part 2:
    # display_segments = {
    #     0: ["a", "b", "c", "e", "f", "g"],
    #     1: ["c", "f"],
    #     2: ["a", "c", "d", "e", "g"],
    #     3: ["a", "c", "d", "f", "g"],
    #     4: ["b", "c", "d", "f"],
    #     5: ["a", "b", "d", "f", "g"],
    #     6: ["a", "b", "d", "e", "f", "g"],
    #     7: ["a", "c", "f"],
    #     8: ["a", "b", "c", "d", "e", "f", "g"],
    #     9: ["a", "b", "c", "d", "f", "g"],
    # }

    part_two = 0
    with open("day_8_input.txt") as f:
        for line in f.readlines():
            new_segments = dict()
            left, right = line.split(" | ")
            # Identify the numbers we already know by their unique length of segments
            for word in left.split():
                if len(word) == 2:
                    new_segments[1] = set(word)
                elif len(word) == 3:
                    new_segments[7] = set(word)
                elif len(word) == 4:
                    new_segments[4] = set(word)
                elif len(word) == 7:
                    new_segments[8] = set(word)
            # Get the rest of numbers operating with sets of characters to match missing ones
            e_and_g = new_segments[8] - new_segments[7] - new_segments[4]
            for word in left.split():
                if len(word) == 6:
                    if set(word).union(e_and_g) == new_segments[8]:
                        new_segments[9] = set(word)
                    elif set(word).union(new_segments[7]) == new_segments[8]:
                        new_segments[6] = set(word)
                    else:
                        new_segments[0] = set(word)
                elif len(word) == 5:
                    if len(set(word) - e_and_g) == 3:
                        new_segments[2] = set(word)
                    elif len(set(word) - new_segments[1]) == 3:
                        new_segments[3] = set(word)
                    else:
                        new_segments[5] = set(word)
            # Get the displayed number and add it to the result
            display_number = str()
            for word in right.split():
                for i, s in new_segments.items():
                    if set(word) == s:
                        display_number += str(i)
                        break
            part_two += int(display_number)
    print(f"Part 2: {part_two}")


if __name__ == "__main__":
    main()
