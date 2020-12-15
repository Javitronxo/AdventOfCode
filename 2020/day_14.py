import re
from itertools import product


def main():
    memory_pattern = r"mem\[(\d+)\] = (\d+)"

    reverse_mask = None
    memory = dict()
    with open("day_14_input.txt") as f:
        for line in f.read().splitlines():
            if "mask" in line:
                reverse_mask = line.split(" = ")[1][::-1]
            else:
                address, value = re.findall(memory_pattern, line)[0]
                reverse_bin_value = bin(int(value))[2:][::-1]
                new_value = ""
                for i, char in enumerate(reverse_mask):
                    if char == "X":
                        try:
                            new_value += reverse_bin_value[i]
                        except IndexError:
                            new_value += "0"
                    else:
                        new_value += char
                memory[address] = int(new_value[::-1], 2)
    print(f"Part 1: {sum(list(memory.values()))}")

    reverse_mask = None
    memory = dict()
    with open("day_14_input.txt") as f:
        for line in f.read().splitlines():
            if "mask" in line:
                reverse_mask = line.split(" = ")[1][::-1]
            else:
                address, value = re.findall(memory_pattern, line)[0]
                reverse_bin_address = bin(int(address))[2:][::-1]
                new_address = ""
                for i, char in enumerate(reverse_mask):
                    if char == "0":
                        try:
                            new_address += reverse_bin_address[i]
                        except IndexError:
                            new_address += "0"
                    elif char == "1":
                        new_address += "1"
                    else:
                        new_address += "X"
                new_address = new_address[::-1]
                new_addresses = list()
                for combination in product([0, 1], repeat=new_address.count("X")):
                    i = 0
                    address = ""
                    for char in new_address:
                        if char == "X":
                            address += str(combination[i])
                            i += 1
                        else:
                            address += char
                    new_addresses.append(address)
                for address in new_addresses:
                    memory[address] = int(value)
    print(f"Part 2: {sum(list(memory.values()))}")


if __name__ == "__main__":
    main()
