from collections import defaultdict


def main():
    with open('day_10_input.txt') as f:
        input_lines = [int(x) for x in f.read().splitlines()]

    adapters = [0] + sorted(input_lines)
    adapters.append(adapters[-1] + 3)

    differences = defaultdict(int)
    for i in range(len(adapters) - 1):
        differences[adapters[i + 1] - adapters[i]] += 1
    print(f"Part 1: {differences[1] * differences[3]}")

    connections = defaultdict(int)
    connections[0] = 1
    for adapter in adapters[1:]:
        connections[adapter] = sum([connections[adapter - i] for i in range(1, 4)])
    print(f"Part 2: {connections[adapters[-1]]}")


if __name__ == '__main__':
    main()
