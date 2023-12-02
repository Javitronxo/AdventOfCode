import re


class Game:
    def __init__(self, line: str):
        self.id = 0
        self.games = list()
        self.new_game(line)

    def new_game(self, line: str):
        game_id_str, games_str = line.split(": ")
        self.id = int(re.match(r"Game (\d+)", game_id_str).group(1))

        for i, game in enumerate(games_str.split("; ")):
            self.games.append(dict())
            parts = game.split(", ")
            for part in parts:
                num_cubes, color = part.split()
                self.games[i][color] = int(num_cubes)

    def is_possible(self, bag):
        for game in self.games:
            for color, num_cubes in game.items():
                if num_cubes > bag[color]:
                    return False
        return True

    @property
    def power(self):
        bag = {"green": 0, "red": 0, "blue": 0}
        for game in self.games:
            for color, num_cubes in game.items():
                if num_cubes > bag[color]:
                    bag[color] = num_cubes
        return bag["green"] * bag["red"] * bag["blue"]


def main():
    max_bag = {"green": 13, "red": 12, "blue": 14}
    with open("day_2_input.txt") as f:
        possible_games = list()
        games_power = list()
        for line in f.readlines():
            game = Game(line)
            if game.is_possible(max_bag):
                possible_games.append(game.id)
            games_power.append(game.power)
    print(f"Part 1: {sum(possible_games)}")
    print(f"Part 1: {sum(games_power)}")


if __name__ == "__main__":
    main()
