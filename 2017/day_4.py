def main():
    valid_passwords_one = 0
    valid_passwords_two = 0
    with open("day_4_input.txt") as f:
        for line in f.read().splitlines():
            words_list = line.split()
            sorted_words_list = ["".join(sorted(word)) for word in words_list]
            if len(words_list) == len(set(words_list)):
                valid_passwords_one += 1
            if len(words_list) == len(set(sorted_words_list)):
                valid_passwords_two += 1

    print(f"Part 1: {valid_passwords_one}")
    print(f"Part 2: {valid_passwords_two}")


if __name__ == "__main__":
    main()
