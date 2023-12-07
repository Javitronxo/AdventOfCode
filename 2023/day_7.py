from __future__ import annotations

from dataclasses import dataclass

ORDER_PART_ONE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
ORDER_PART_TWO = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


@dataclass
class Game:
    cards: str
    bid: int
    part_one: bool = True

    def __post_init__(self):
        self.order = ORDER_PART_ONE if self.part_one else ORDER_PART_TWO

        self.cards_dict = dict()
        for char in self.cards:
            try:
                self.cards_dict[char] += 1
            except KeyError:
                self.cards_dict[char] = 1

        if not self.part_one and "J" in self.cards_dict and 0 < (num_j := self.cards_dict["J"]) < 5:
            del self.cards_dict["J"]
            max_value = max(self.cards_dict.values())
            for char in self.order:
                if char in self.cards_dict and self.cards_dict[char] == max_value:
                    self.cards_dict[char] += num_j
                    break

        if len(self.cards_dict.keys()) == 1:
            self.hand = 7  # "FIVE OF A KIND"
        elif sorted(list(self.cards_dict.values())) == [1, 4]:
            self.hand = 6  # "FOUR OF A KIND"
        elif sorted(list(self.cards_dict.values())) == [2, 3]:
            self.hand = 5  # "FULL HOUSE"
        elif sorted(list(self.cards_dict.values())) == [1, 1, 3]:
            self.hand = 4  # "THREE OF A KIND"
        elif sorted(list(self.cards_dict.values())) == [1, 2, 2]:
            self.hand = 3  # "TWO PAIR"
        elif sorted(list(self.cards_dict.values())) == [1, 1, 1, 2]:
            self.hand = 2  # "ONE PAIR"
        elif len(self.cards_dict.keys()) == 5:
            self.hand = 1  # "HIGH CARD"

    def __lt__(self, other: Game) -> bool:
        if self.hand < other.hand:
            return True
        elif self.hand > other.hand:
            return False
        for i, char in enumerate(self.cards):
            if self.order.index(char) > self.order.index(other.cards[i]):
                return True
            elif self.order.index(char) < self.order.index(other.cards[i]):
                return False


def main():
    games_part_one = list()
    games_part_two = list()
    with open("day_7_input.txt") as f:
        for line in f.readlines():
            cards, bid = line.strip().split()
            games_part_one.append(Game(cards, int(bid)))
            games_part_two.append(Game(cards, int(bid), part_one=False))

    part_one = [(i + 1) * game.bid for i, game in enumerate(sorted(games_part_one))]
    print(f"Part 1: {sum(part_one)}")

    part_two = [(i + 1) * game.bid for i, game in enumerate(sorted(games_part_two))]
    print(f"Part 2: {sum(part_two)}")


if __name__ == "__main__":
    main()
