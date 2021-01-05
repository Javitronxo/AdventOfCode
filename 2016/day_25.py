def main():
    """
    This time I did not come with an algorithm to read and solve the puzzle.
    Instead I read the puzzle input and solved it manually, reaching the generalization below.
    """
    magic_number = 15 * 170  # Number of iterations in the first loop of the puzzle input
    answer = 0
    while True:
        is_right = True
        bin_str = bin(magic_number + answer)[2:]
        for i in range(len(bin_str) - 1):
            if bin_str[i] == bin_str[i + 1]:
                is_right = False
                break
        if is_right:
            break
        answer += 1
    print(f"Part 1: {answer}")


if __name__ == "__main__":
    main()
