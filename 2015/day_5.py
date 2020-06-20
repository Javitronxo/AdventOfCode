def is_nicer_string(input_str: str) -> bool:
    letter_repeats_two_hops = False
    duplicate_pair = False
    for i in range(len(input_str) - 2):
        if input_str[i] == input_str[i + 2]:
            letter_repeats_two_hops = True

        pair = input_str[i] + input_str[i + 1]
        if pair in input_str[:i] + '-' + input_str[i + 2:]:
            duplicate_pair = True

        if letter_repeats_two_hops and duplicate_pair:
            return True

    return False


def is_nice_string(input_str: str) -> bool:
    disallowed_pairs = ['ab', 'cd', 'pq', 'xy']
    if True in [pair in input_str for pair in disallowed_pairs]:
        return False

    contiguous_letters = False
    n_vowels = 0
    for i in range(len(input_str) - 1):
        if input_str[i] in 'aeiou':
            n_vowels += 1
        if not contiguous_letters and input_str[i] == input_str[i + 1]:
            contiguous_letters = True
    if input_str[-1] in 'aeiou':
        n_vowels += 1

    if n_vowels >= 3 and contiguous_letters:
        return True
    return False


def main():
    nice_strings = 0
    nicer_strings = 0
    with open('day_5_input.txt') as f_in:
        for input_str in f_in.readlines():
            if is_nice_string(input_str.strip()):
                nice_strings += 1
            if is_nicer_string(input_str.strip()):
                nicer_strings += 1
    print('Santa found %d nice strings' % nice_strings)
    print('Santa found %d even nicer strings' % nicer_strings)


if __name__ == '__main__':
    main()
