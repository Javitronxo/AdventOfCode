import re
from collections import defaultdict
from string import ascii_lowercase as alphabet
from typing import Union, List


class Room:
    def __init__(self, name: List[str], sector: Union[str, int], checksum: str):
        self.name = name
        self.sector = int(sector)
        self.checksum = checksum

    def is_real_room(self) -> bool:
        letter_count = defaultdict(int)
        for word in self.name:
            for char in word:
                letter_count[char] += 1
        ordered_letters = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[0])}
        ordered_letters = {k: v for k, v in sorted(ordered_letters.items(), key=lambda item: item[1], reverse=True)}
        if self.checksum == "".join(list(ordered_letters.keys())[: len(self.checksum)]):
            return True
        return False

    def decrypt_room_name(self) -> str:
        room_name = str()
        for word in self.name:
            for char in word:
                new_index = (alphabet.index(char) + self.sector) % len(alphabet)
                room_name += alphabet[new_index]
            room_name += " "
        return room_name.strip()


def main():
    real_sector_ids = list()
    room_names = dict()

    with open("day_4_input.txt") as f_in:
        for line in f_in.readlines():
            name = line.split("-")[:-1]
            sector, checksum = re.search(r"(\d+)\[(\w+)\]", line).groups()
            room = Room(name, sector, checksum)

            if room.is_real_room():
                real_sector_ids.append(int(sector))
                room_names[room.decrypt_room_name()] = sector

    print(f"Part 1: The sum of the sector IDs of the real rooms is {sum(real_sector_ids)}")

    target_room = "northpole object storage"
    print(f"Part 2: The sector ID of the room where North Pole objects are stored is {room_names[target_room]}")


if __name__ == "__main__":
    main()
