# https://adventofcode.com/2019/day/2
import lib.utils as utils


def int_code_processor(memory):
    pointer = 0
    while memory[pointer] != 99:
        code = memory[pointer]
        noun = memory[memory[pointer + 1]]
        verb = memory[memory[pointer + 2]]
        position = memory[pointer + 3]
        if code == 1:
            memory[position] = noun + verb
        elif code == 2:
            memory[position] = noun * verb
        pointer += 4

    return memory[0]


def first_part(memory):
    memory[1] = 12
    memory[2] = 2
    output = int_code_processor(memory)
    return output


def second_part(memory):
    target_output = 19690720
    for i in range(100):
        for j in range(100):
            tmp_memory = memory[:]
            tmp_memory[1] = i
            tmp_memory[2] = j
            output = int_code_processor(tmp_memory)
            if output == target_output:
                return 100 * i + j


def main():
    memory = utils.read_file_to_int_list('day_2_input.txt')
    result_first_part = first_part(memory[:])
    print("First part result: {}".format(result_first_part))
    result_second_part = second_part(memory[:])
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
