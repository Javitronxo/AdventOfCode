def generate_data(data: str) -> str:
    b = data[::-1]
    xor_b = bin(int(b, 2) ^ int("1" * len(b), 2))[2:]
    new_b = "0" * (len(b) - len(xor_b)) + xor_b
    return data + "0" + new_b


def get_checksum(data: str) -> str:
    checksum = str()
    for i in range(0, len(data) - 1, 2):
        checksum += "1" if data[i] == data[i + 1] else "0"
    return checksum


def solve(input_data: str, disk_length: int) -> str:
    data = generate_data(input_data)
    while len(data) < disk_length:
        data = generate_data(data)

    checksum = get_checksum(data[:disk_length])
    while len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)

    return checksum


def main():
    with open("day_16_input.txt") as f:
        puzzle_input = f.read().strip()

    disk_length = 272
    print(f"Part 1: {solve(puzzle_input, disk_length)}")

    disk_length = 35651584
    print(f"Part 2: {solve(puzzle_input, disk_length)}")


if __name__ == "__main__":
    main()
