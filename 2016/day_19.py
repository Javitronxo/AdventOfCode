from typing import List


class Elf:
    """Node for a circular linked list"""

    def __init__(self, number: int):
        self.number = number
        self.previous = None
        self.next = None

    def remove(self):
        self.next.previous = self.previous
        self.previous.next = self.next


def get_dutch_rudder(puzzle_input: int) -> List[Elf]:
    """Create a circular linked list of elves"""
    dutch_rudder = [Elf(0)]
    for i in range(1, puzzle_input):
        elf = Elf(i)
        elf.previous = dutch_rudder[-1]
        dutch_rudder[-1].next = elf
        dutch_rudder.append(elf)
    dutch_rudder[0].previous = dutch_rudder[-1]
    dutch_rudder[-1].next = dutch_rudder[0]
    return dutch_rudder


def main():
    with open("day_19_input.txt") as f:
        puzzle_input = int(f.read())

    dutch_rudder = get_dutch_rudder(puzzle_input)
    head = dutch_rudder[0]
    while True:
        if head == head.next == head.previous:
            break
        head = head.next
        head.remove()
        head = head.next
    print(f"Part 1: {head.number + 1}")

    dutch_rudder = get_dutch_rudder(puzzle_input)
    head = dutch_rudder[0]
    center = dutch_rudder[puzzle_input // 2]
    for i in range(puzzle_input - 1):
        center.remove()
        center = center.next
        if (puzzle_input - i) % 2 == 1:
            center = center.next
        head = head.next
    print(f"Part 2: {head.number + 1}")


if __name__ == "__main__":
    main()
