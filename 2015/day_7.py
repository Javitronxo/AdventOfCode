class Gate:
    def __init__(self, output_cable: str, input_parts: list):
        self.output_cable = output_cable
        self.right_input = input_parts.pop(-1)
        self.operation = input_parts.pop(-1) if len(input_parts) else None
        self.left_input = input_parts.pop(-1) if len(input_parts) else None
        self.output_value = None

    @staticmethod
    def get_output_value(right: int, operation: str, left: int = None) -> int:
        if operation == 'AND':
            output = left & right
        elif operation == 'OR':
            output = left | right
        elif operation == 'RSHIFT':
            output = left >> right
        elif operation == 'LSHIFT':
            output = left << right
        elif operation == 'NOT':
            output = ~ right
        else:
            raise ValueError
        return output


def get_gates(instructions: list) -> list:
    gates = list()
    for instruction in instructions:
        input_part, output_part = instruction.split(' -> ')
        input_parts = input_part.split()
        gate = Gate(output_part, input_parts)
        gates.append(gate)
    return gates


def get_output_values(gates: list) -> list:
    output_values = dict()
    while len([gate for gate in gates if gate.output_value is None]):
        print('Still have %d gates without output value' % len([gate for gate in gates if gate.output_value is None]))
        for gate in gates:
            # No operator
            if gate.operation is None and (gate.right_input.isdigit() or gate.right_input in output_values):
                gate.output_value = gate.right_input if gate.right_input.isdigit() else output_values[gate.right_input]
                output_values[gate.output_cable] = gate.output_value
                continue

            # NOT operator
            if gate.right_input in output_values and not gate.left_input and gate.operation:
                output_value = Gate.get_output_value(output_values[gate.right_input], gate.operation)
                gate.output_value = output_value
                output_values[gate.output_cable] = output_value
                continue

            # All the other operators
            if (gate.right_input.isdigit() or gate.right_input in output_values) and \
                    (gate.left_input.isdigit() or gate.left_input in output_values):
                right_value = gate.right_input if gate.right_input.isdigit() else output_values[gate.right_input]
                left_value = gate.left_input if gate.left_input.isdigit() else output_values[gate.left_input]
                output_value = Gate.get_output_value(int(right_value), gate.operation, int(left_value))
                gate.output_value = output_value
                output_values[gate.output_cable] = output_value
                continue

    return gates


def main():
    instructions = list()
    with open('day_7_input.txt') as f_in:
        for line in f_in.readlines():
            instructions.append(line.strip())

    gates = get_gates(instructions)
    gates = get_output_values(gates)
    wire_a_output = [gate for gate in gates if gate.output_cable == 'a'][0].output_value
    print('Signal provided to wire a is: %s' % wire_a_output)

    gates = get_gates(instructions)
    for gate in gates:
        if gate.output_cable == 'b':
            gate.right_input = str(wire_a_output)
            break
    gates = get_output_values(gates)
    wire_a_output = [gate for gate in gates if gate.output_cable == 'a'][0].output_value
    print('Signal provided to wire a is: %s' % wire_a_output)


if __name__ == '__main__':
    main()
