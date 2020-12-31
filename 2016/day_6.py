def main():
    input_list = list()
    with open("day_6_input.txt") as f_in:
        for line in f_in.readlines():
            input_list.append(line.strip())

    target_word_1 = str()
    target_word_2 = str()
    word_length = len(input_list[0])

    for i in range(word_length):
        max_char_count = 0
        min_char_count = len(input_list) + 1
        target_char_1 = None
        target_char_2 = None

        chars = [word[i] for word in input_list]
        for char in chars:
            char_count = chars.count(char)
            if char_count > max_char_count:
                max_char_count = char_count
                target_char_1 = char
            if char_count < min_char_count:
                min_char_count = char_count
                target_char_2 = char

        target_word_1 += target_char_1
        target_word_2 += target_char_2

    print(f"Part 1: The error-corrected version of the message being sent is {target_word_1}")
    print(f"Part 2: The error-corrected version of the message being sent is {target_word_2}")


if __name__ == "__main__":
    main()
