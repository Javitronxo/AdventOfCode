from lib.assembunny_2016 import run_program


def main():
    with open("day_23_input.txt") as f:
        instructions = f.read().splitlines()
        instructions_copy = instructions[:]

    print(f"Part 1: {run_program(instructions, 7)}")

    # In the input instructions there is a double for loop between instructions 4 to 9:
    #     cpy b c
    #     inc a
    #     dec c
    #     jnz c -2
    #     dec d
    #     jnz d -5
    # It increases "a" by one a number of times equal to "b" * "d"
    # From description: "You wonder what's taking so long, and whether the lack of any instruction more powerful
    #   than "add one" has anything to do with it. Don't bunnies usually multiply?"
    # Modify the input to do the multiplication without the loop by adding "mul" and "nop" instructions.
    instructions = instructions_copy
    instructions[4] = "mul a b d"
    instructions[5] = "cpy 0 c"
    instructions[6] = "cpy 0 d"
    instructions[7] = instructions[8] = instructions[9] = "nop"
    print(f"Part 2: {run_program(instructions, 12)}")


if __name__ == "__main__":
    main()
