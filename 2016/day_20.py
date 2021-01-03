def main():
    with open("day_20_input.txt") as f:
        ip_ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in f.read().splitlines()]

    ip_ranges.sort(key=lambda x: x[0])
    allowed_ip_ranges = list()
    _, upper_end = ip_ranges.pop(0)
    for start, end in ip_ranges:
        if start > upper_end + 1:
            allowed_ip_ranges.append((upper_end + 1, start - 1))
            upper_end = end
        elif upper_end < end:
            upper_end = end

    print(f"Part 1: {allowed_ip_ranges[0][0]}")
    print(f"Part 2: {sum(end + 1 - start for start, end in allowed_ip_ranges)}")


if __name__ == "__main__":
    main()
