def main():
    with open("day_4_input.txt") as f:
        total_overlap = 0
        partial_overlap = 0
        for line in f.readlines():
            section_1, section_2 = line.split(",")
            section_1 = [int(char) for char in section_1.split("-")]
            section_2 = [int(char) for char in section_2.split("-")]
            if (section_1[0] <= section_2[0] and section_1[1] >= section_2[1]) or (
                section_2[0] <= section_1[0] and section_2[1] >= section_1[1]
            ):
                total_overlap += 1
            if (
                (section_2[0] <= section_1[0] <= section_2[1])
                or (section_2[0] <= section_1[1] <= section_2[1])
                or (section_1[0] <= section_2[0] <= section_1[1])
                or (section_1[0] <= section_2[1] <= section_1[1])
            ):
                partial_overlap += 1

    print(f"Part 1: {total_overlap}")
    print(f"Part 2: {partial_overlap}")


if __name__ == "__main__":
    main()
