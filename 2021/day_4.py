from typing import List


class BingoCard:
    def __init__(self, lines: List[str]):
        self.grid = self._get_grid(lines)

    @staticmethod
    def _get_grid(lines: List[str]) -> List[List[str]]:
        grid = list()
        for i, line in enumerate(lines):
            grid.append(list())
            for n in line.split():
                grid[i].append(int(n))
        return grid

    @property
    def is_bingo(self) -> bool:
        for row in self.grid:
            if set(row) == {"#"}:
                return True
        for column in zip(*self.grid):
            if set(column) == {"#"}:
                return True
        return False

    def mark(self, number: int) -> bool:
        for i, line in enumerate(self.grid):
            for j, n in enumerate(line):
                if number == n:
                    self.grid[i][j] = "#"
                    return self.is_bingo

    def get_score(self, number: int) -> int:
        return sum(n for line in self.grid for n in line if n != "#") * number


def main():
    bingo_cards = list()
    with open("day_4_input.txt") as f:
        card_rows = list()
        for i, line in enumerate(f.readlines()):
            if i == 0:
                numbers = [int(x) for x in line.split(",")]
                continue
            if not len(line.strip()):
                if card_rows:
                    bingo_cards.append(BingoCard(card_rows))
                    card_rows = list()
                continue
            card_rows.append(line.strip())
        bingo_cards.append(BingoCard(card_rows))

    part_one_solved = False
    for number in numbers:
        has_bingo = list()
        for bingo_card in bingo_cards:
            if bingo_card.mark(number):
                has_bingo.append(bingo_card)
        while len(has_bingo):
            bingo_card = has_bingo.pop()
            bingo_cards.remove(bingo_card)
            if not part_one_solved:
                print(f"Part 1: {bingo_card.get_score(number)}")
                part_one_solved = True
            if not len(bingo_cards):
                print(f"Part 2: {bingo_card.get_score(number)}")


if __name__ == '__main__':
    main()
