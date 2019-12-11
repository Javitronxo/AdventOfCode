import copy


class IntCodeProcessor:
    def __init__(self, memory):
        self.pointer = 0
        self.relative_base = 0
        self.memory = copy.deepcopy(memory)
        self.inputs = list()
        self.outputs = list()
        self.status = "IDLE"

    def add_input(self, new_input):
        self.inputs.append(new_input)
        self.run()

    def get_parameters(self, instruction):
        code = instruction[-1]
        a, b, c = instruction[:3]
        arg1, arg2, arg3 = None, None, None
        if c == 0:
            arg1 = self.memory[self.memory[self.pointer + 1]]
        elif c == 1:
            arg1 = self.memory[self.pointer + 1]
        elif c == 2:
            arg1 = self.memory[self.memory[self.pointer + 1] + self.relative_base]
        if b == 0:
            arg2 = self.memory[self.memory[self.pointer + 2]]
        elif b == 1:
            arg2 = self.memory[self.pointer + 2]
        elif b == 2:
            arg2 = self.memory[self.memory[self.pointer + 2] + self.relative_base]
        if a == 0:
            arg3 = self.memory[self.pointer + 3]
        elif a == 1:
            arg3 = self.pointer + 3
        elif a == 2:
            arg3 = self.memory[self.pointer + 3] + self.relative_base
        return code, arg1, arg2, arg3

    def run(self):
        self.status = "RUNNING"
        while self.memory[self.pointer] != 99:
            instruction = [int(x) for x in str(self.memory[self.pointer]).zfill(5)]
            code, arg1, arg2, arg3 = self.get_parameters(instruction)

            if code in [1, 2, 7, 8]:
                if code == 1:
                    self.memory[arg3] = arg1 + arg2
                elif code == 2:
                    self.memory[arg3] = arg1 * arg2
                elif code == 7:
                    self.memory[arg3] = 1 if arg1 < arg2 else 0
                elif code == 8:
                    self.memory[arg3] = 1 if arg1 == arg2 else 0
                self.pointer += 4
            elif code == 3:
                if not len(self.inputs):
                    self.status = "WAITING"
                    return
                position = self.memory[self.pointer + 1] + self.relative_base if instruction[-3] else \
                    self.memory[self.pointer + 1]
                self.memory[position] = self.inputs.pop(0)
                self.pointer += 2
            elif code in [4, 9]:
                if code == 4:
                    self.outputs.append(arg1)
                elif code == 9:
                    self.relative_base += arg1
                self.pointer += 2
            elif code in [5, 6]:
                if (code == 5 and arg1 != 0) or (code == 6 and arg1 == 0):
                    self.pointer = arg2
                else:
                    self.pointer += 3
        self.status = "COMPLETED"
