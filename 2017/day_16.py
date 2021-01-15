from typing import List


def dance(positions: str, instructions: List[str]) -> str:
    for instruction in instructions:
        operation = instruction[0]
        if operation == "x":
            a, b = [int(x) for x in instruction[1:].split("/")]
            _positions = str()
            for i, char in enumerate(positions):
                if i == a:
                    _positions += positions[b]
                elif i == b:
                    _positions += positions[a]
                else:
                    _positions += char
            positions = _positions
        elif operation == "s":
            offset = int(instruction[1:])
            positions = positions[-offset:] + positions[:-offset]
        elif operation == "p":
            a, b = instruction[1:].split("/")
            _positions = str()
            for char in positions:
                if char == a:
                    _positions += b
                elif char == b:
                    _positions += a
                else:
                    _positions += char
            positions = _positions
        else:
            raise ValueError(f"Unrecognized operation: {operation}")
    return positions


def main():
    positions = "abcdefghijklmnop"
    with open("day_16_input.txt") as f:
        instructions = f.read().split(",")
    visited_positions = [positions]

    positions = dance(positions, instructions)
    visited_positions.append(positions)
    print(f"Part 1: {positions}")

    n_times = 1_000_000_000
    for i in range(n_times - 1):
        positions = dance(positions, instructions)
        if positions in visited_positions:
            break
        visited_positions.append(positions)
    print(f"Part 2: {visited_positions[n_times % len(visited_positions)]}")


if __name__ == "__main__":
    main()
