def main():
    char_pairs = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }
    score_syntax = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score_incomplete = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    syntax_error_score = 0
    completion_scores = list()
    with open("day_10_input.txt") as f:
        for line in f.readlines():
            stack = list()
            corrupted = False
            completion_score = 0
            for char in line.strip():
                if char in char_pairs.keys():
                    stack.append(char)
                else:
                    last_char = stack.pop()
                    if char != char_pairs[last_char]:
                        syntax_error_score += score_syntax[char]
                        corrupted = True
                        break
            if not corrupted:
                while stack:
                    char = stack.pop()
                    completion_score = completion_score * 5 + score_incomplete[char_pairs[char]]
                completion_scores.append(completion_score)

    print(f"Part 1: {syntax_error_score}")
    print(f"Part 2: {sorted(completion_scores)[len(completion_scores) // 2]}")


if __name__ == "__main__":
    main()
