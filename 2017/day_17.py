from collections import deque


def run(n_times: int, n_steps: int) -> deque:
    circular_buffer = deque([0])
    for i in range(1, n_times + 1):
        circular_buffer.rotate(-n_steps)
        circular_buffer.append(i)
    return circular_buffer


def main():
    with open("day_17_input.txt") as f:
        n_steps = int(f.read().strip())

    n_times = 2017
    circular_buffer = run(n_times, n_steps)
    print(f"Part 1: {circular_buffer.popleft()}")

    n_times = 50_000_000
    circular_buffer = run(n_times, n_steps)
    circular_buffer.rotate(-circular_buffer.index(0))
    circular_buffer.popleft()
    print(f"Part 2: {circular_buffer.popleft()}")


if __name__ == "__main__":
    main()
