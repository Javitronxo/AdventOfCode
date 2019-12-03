# https://adventofcode.com/2019/day/2


def read_input_file(file_name):
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(',')]
    return input_list


def int_code_processor(memory):
    i = 0
    while i < len(memory):
        opcode = memory[i]
        if opcode == 99:
            return memory[0]
        try:
            noun_address = memory[i + 1]
            verb_address = memory[i + 2]
            noun = memory[noun_address]
            verb = memory[verb_address]
            position = memory[i + 3]
            i += 4

            if opcode == 1:
                memory[position] = noun + verb
            elif opcode == 2:
                memory[position] = noun * verb
            else:
                print("Unrecognized opcode: {}".format(opcode))

        except IndexError:
            print("Index Error!?")
            return None

    return memory[0]


def first_part(file_name):
    memory = read_input_file(file_name)
    memory[1] = 12
    memory[2] = 2
    output = int_code_processor(memory)
    return output


def second_part(file_name):
    target_output = 19690720
    memory = read_input_file(file_name)

    for i in range(100):
        for j in range(100):
            tmp_memory = memory[:]
            tmp_memory[1] = i
            tmp_memory[2] = j
            output = int_code_processor(tmp_memory)
            if output == target_output:
                return 100 * i + j


def main():
    file_name = 'day_2_input.txt'
    result_first_part = first_part(file_name)
    print("First part result: {}".format(result_first_part))
    result_second_part = second_part(file_name)
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
