def main():
    ingredient_ranges = []
    part_1 = 0

    with open("day_5_input.txt") as f:
        for line in f.readlines():
            if "-" in line:
                range_ends = [int(x) for x in line.split("-")]
                ingredient_ranges.append((range_ends[0], range_ends[1]))
            elif line.strip() == "":
                continue
            else:
                for ingredient_range in ingredient_ranges:
                    if ingredient_range[0] <= int(line.strip()) <= ingredient_range[1]:
                        part_1 += 1
                        break

    print(f"Part 1: {part_1}")

    part_2 = 0
    ingredient_ranges.sort()
    max_end = 0
    for start, end in ingredient_ranges:
        if end >= max_end:
            part_2 += end - max(start, max_end) + 1
            max_end = end + 1

    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
