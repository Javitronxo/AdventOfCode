from collections import deque
from typing import List, Tuple

from lib.utils import read_file_to_int_list


def run(numbers_queue: deque, lengths: List[int], position: int = 0, skip_size: int = 0) -> Tuple[deque, int, int]:
    for length in lengths:
        numbers_list = list(numbers_queue)
        numbers_queue = deque(numbers_list[:length][::-1] + numbers_list[length:])
        rotation = (length + skip_size) % len(numbers_queue)
        position += length + skip_size
        numbers_queue.rotate(-rotation)
        skip_size += 1
    return numbers_queue, position, skip_size


def main():
    lengths = read_file_to_int_list("day_10_input.txt")
    numbers_deque = deque(range(256))
    numbers_deque, current_position, _ = run(numbers_deque, lengths)
    numbers_deque.rotate(current_position)
    print(f"Part 1: {numbers_deque.popleft() * numbers_deque.popleft()}")

    lengths = list()
    with open("day_10_input.txt") as f:
        for char in f.read().strip():
            lengths.append(ord(char))
    lengths.extend([17, 31, 73, 47, 23])
    numbers_deque = deque(range(256))

    total_rounds = 64
    current_position = 0
    skip_size = 0
    for _ in range(total_rounds):
        numbers_deque, current_position, skip_size = run(numbers_deque, lengths, current_position, skip_size)
    numbers_deque.rotate(current_position)

    dense_hash_numbers = list()
    while numbers_deque:
        xor_result = 0
        for _ in range(16):
            xor_result = xor_result ^ numbers_deque.popleft()
        dense_hash_numbers.append(xor_result)

    dense_hash = str()
    for n in dense_hash_numbers:
        hex_n = hex(n).split("x")[-1]
        if len(hex_n) == 1:
            dense_hash += "0"
        dense_hash += hex_n
    print(f"Part 2: {dense_hash}")


if __name__ == "__main__":
    main()
