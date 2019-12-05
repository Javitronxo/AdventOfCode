# https://adventofcode.com/2019/day/5
import lib.utils as utils


def int_code_processor(memory, input_code):
    pointer = 0
    output = None

    while memory[pointer] != 99:
        instruction = [int(x) for x in str(memory[pointer]).zfill(5)]
        code = instruction[-1]
        a, b, c = instruction[:3]

        if code in [1, 2, 7, 8]:
            noun = memory[pointer + 1] if c else memory[memory[pointer + 1]]
            verb = memory[pointer + 2] if b else memory[memory[pointer + 2]]
            position = pointer + 3 if a else memory[pointer + 3]
            if code == 1:
                memory[position] = noun + verb
            elif code == 2:
                memory[position] = noun * verb
            elif code == 7:
                memory[position] = 1 if noun < verb else 0
            elif code == 8:
                memory[position] = 1 if noun == verb else 0
            pointer += 4
        elif code == 3:
            position = memory[pointer + 1]
            memory[position] = input_code
            pointer += 2
        elif code == 4:
            position = pointer + 1 if c else memory[pointer + 1]
            output = memory[position]
            pointer += 2
        elif code in [5, 6]:
            noun = memory[pointer + 1] if c else memory[memory[pointer + 1]]
            verb = memory[pointer + 2] if b else memory[memory[pointer + 2]]
            if (code == 5 and noun != 0) or (code == 6 and noun == 0):
                pointer = verb
            else:
                pointer += 3

    return output


def main():
    memory = utils.read_file_to_int_list('day_5_input.txt')
    result_first_part = int_code_processor(memory[:], 1)
    print("First part result: {}".format(result_first_part))
    result_second_part = int_code_processor(memory[:], 5)
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
