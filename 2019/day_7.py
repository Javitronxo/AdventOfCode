# https://adventofcode.com/2019/day/7
from itertools import permutations

import lib.utils as utils


class IntCodeProcessor:
    def __init__(self, memory):
        self.pointer = 0
        self.memory = memory[:]
        self.inputs = list()
        self.outputs = list()
        self.status = "IDLE"

    def add_input(self, new_input):
        self.inputs.append(new_input)
        self.run()

    def run(self):
        self.status = "RUNNING"
        while self.memory[self.pointer] != 99:
            instruction = [int(x) for x in str(self.memory[self.pointer]).zfill(5)]
            code = instruction[-1]
            a, b, c = instruction[:3]

            if code in [1, 2, 7, 8]:
                noun = self.memory[self.pointer + 1] if c else self.memory[self.memory[self.pointer + 1]]
                verb = self.memory[self.pointer + 2] if b else self.memory[self.memory[self.pointer + 2]]
                position = self.pointer + 3 if a else self.memory[self.pointer + 3]
                if code == 1:
                    self.memory[position] = noun + verb
                elif code == 2:
                    self.memory[position] = noun * verb
                elif code == 7:
                    self.memory[position] = 1 if noun < verb else 0
                elif code == 8:
                    self.memory[position] = 1 if noun == verb else 0
                self.pointer += 4
            elif code == 3:
                if not len(self.inputs):
                    self.status = "WAITING"
                    return
                position = self.memory[self.pointer + 1]
                self.memory[position] = self.inputs.pop(0)
                self.pointer += 2
            elif code == 4:
                position = self.pointer + 1 if c else self.memory[self.pointer + 1]
                self.outputs.append(self.memory[position])
                self.pointer += 2
            elif code in [5, 6]:
                noun = self.memory[self.pointer + 1] if c else self.memory[self.memory[self.pointer + 1]]
                verb = self.memory[self.pointer + 2] if b else self.memory[self.memory[self.pointer + 2]]
                if (code == 5 and noun != 0) or (code == 6 and noun == 0):
                    self.pointer = verb
                else:
                    self.pointer += 3
        self.status = "COMPLETED"


def run_program(memory, permutation_range):
    max_thruster_signal = 0
    for phases in permutations(permutation_range):
        amplifiers = [IntCodeProcessor(memory) for _ in range(5)]
        for phase, amp in zip(phases, amplifiers):
            amp.add_input(phase)
        amplifiers[0].add_input(0)
        while amplifiers[-1].status != "COMPLETED":
            for i in range(len(phases)):
                amplifiers[(i + 1) % 5].add_input(amplifiers[i].outputs[-1])
        if amplifiers[-1].outputs[-1] > max_thruster_signal:
            max_thruster_signal = amplifiers[-1].outputs[-1]
    return max_thruster_signal


def main():
    memory = utils.read_file_to_int_list('day_7_input.txt')
    result_first_part = run_program(memory, range(5))
    print("First part result: {}".format(result_first_part))
    result_second_part = run_program(memory, range(5, 10))
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
