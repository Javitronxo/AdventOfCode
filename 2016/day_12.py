from lib.assembunny_2016 import run_program


def main():
    with open("day_12_input.txt") as f_in:
        instructions = f_in.readlines()

    print(f"Part 1: {run_program(instructions)}")
    print(f"Part 2: {run_program(instructions, offset_c=1)}")


if __name__ == "__main__":
    main()
