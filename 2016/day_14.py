from typing import List, Tuple, Union

from lib.utils import get_md5_hash


def is_candidate_key(hex_hash: str) -> Tuple[bool, Union[None, str]]:
    """Check if there are 3 consecutive characters in input string"""
    consecutive = 0
    for i in range(len(hex_hash) - 1):
        if hex_hash[i] == hex_hash[i + 1]:
            consecutive += 1
            if consecutive == 2:
                return True, hex_hash[i]
        else:
            consecutive = 0
    return False, None


def get_keys(hashes: List[str], salt: str, stretch_factor: int = None):
    keys = list()
    for index, hex_hash in enumerate(hashes):
        is_candidate, char = is_candidate_key(hex_hash)
        if is_candidate:
            for j, next_hex_hash in enumerate(hashes):
                if j <= index:
                    continue
                elif j > index + 1000:
                    break
                if char * 5 in next_hex_hash:
                    keys.append(hex_hash)
                    break
            if len(keys) == 64:
                return index
        hashes.append(get_md5_hash(salt + str(index + 1000), stretch_factor=stretch_factor))


def main():
    with open("day_14_input.txt") as f:
        puzzle_input = f.read().strip()

    hashes = [get_md5_hash(puzzle_input + str(i)) for i in range(1000)]
    print(f"Part 1: {get_keys(hashes, puzzle_input)}")

    hashes = [get_md5_hash(puzzle_input + str(i), stretch_factor=2016) for i in range(1000)]
    print(f"Part 2: {get_keys(hashes, puzzle_input, stretch_factor=2016)}")


if __name__ == "__main__":
    main()
