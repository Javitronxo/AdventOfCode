def main():
    with open("day_25_input.txt") as f:
        public_keys = [int(x) for x in f.read().splitlines()]

    subject_number = 7
    divisor = 20201227

    loop_sizes = list()
    for public_key in public_keys:
        loop_size = 0
        value = 1
        while value != public_key:
            value = (value * subject_number) % divisor
            loop_size += 1
        loop_sizes.append(loop_size)

    encryption_keys = set()
    for i, public_key in enumerate(reversed(public_keys)):
        loop_size = loop_sizes[i]
        value = 1
        for _ in range(loop_size):
            value = (value * public_key) % divisor
        encryption_keys.add(value)

    assert len(encryption_keys) == 1
    encryption_key = encryption_keys.pop()
    print(f"Part 1: {encryption_key}")


if __name__ == "__main__":
    main()
