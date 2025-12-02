def is_valid_part_1(num_str: str) -> bool:
    return num_str[: len(num_str) // 2] != num_str[len(num_str) // 2 :]


def is_valid_part_2(num_str: str) -> bool:
    for i in range(1, len(num_str) // 2 + 1):
        pattern = num_str[:i]
        if not any(num_str.split(pattern)):
            return False
    return True


def main():
    invalid_ids_1 = []
    invalid_ids_2 = []

    with open("day_2_input.txt") as f:
        product_ranges = f.read().strip().split(",")
        for product_range in product_ranges:
            start, finish = map(int, product_range.split("-"))
            for product_id in range(start, finish + 1):
                if not is_valid_part_1(str(product_id)):
                    invalid_ids_1.append(product_id)
                if not is_valid_part_2(str(product_id)):
                    invalid_ids_2.append(product_id)

    print(f"Part 1: {sum(invalid_ids_1)}")
    print(f"Part 2: {sum(invalid_ids_2)}")


if __name__ == "__main__":
    main()
