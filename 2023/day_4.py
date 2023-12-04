from typing import List


class Card:
    def __init__(self, card_id: int, winning_numbers: List[int], my_numbers: List[int]):
        self.id = card_id
        self.wining_numbers = winning_numbers
        self.my_numbers = my_numbers
        self.count = 1

    @property
    def num_matches(self) -> int:
        return len([i for i in self.my_numbers if i in self.wining_numbers])

    @property
    def points(self) -> int:
        if self.num_matches == 0:
            return 0
        else:
            return 2 ** (self.num_matches - 1)


def main():
    scratchcards = dict()  # Store cards as Dict[card.id, card]

    with open("day_4_input.txt") as f:
        for line in f.readlines():
            # Parse input line
            card_id_str, numbers_str = line.split(": ")
            card_id = int(card_id_str.split()[1])
            wining_numbers_str, my_numbers_str = numbers_str.split(" | ")
            wining_numbers = [int(i) for i in wining_numbers_str.split()]
            my_numbers = [int(i) for i in my_numbers_str.split()]

            # Create and store card
            card = Card(card_id, wining_numbers, my_numbers)
            scratchcards[card_id] = card

    for card_id, card in scratchcards.items():
        for i in range(1, card.num_matches + 1):
            scratchcards[card_id + i].count += card.count

    print(f"Part 1: {sum([card.points for card in scratchcards.values()])}")
    print(f"Part 2: {sum([card.count for card in scratchcards.values()])}")


if __name__ == "__main__":
    main()
