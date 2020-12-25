from typing import List, Tuple

Deck = List[int]


def play_game(player_one_deck: Deck, player_two_deck: Deck, part_two: bool = False) -> Tuple[Deck, bool]:
    played_games = list()

    while player_one_deck and player_two_deck:

        if (player_one_deck, player_two_deck) in played_games:
            return player_one_deck, True
        played_games.append((player_one_deck[:], player_two_deck[:]))

        card_one = player_one_deck.pop(0)
        card_two = player_two_deck.pop(0)

        if part_two and card_one <= len(player_one_deck) and card_two <= len(player_two_deck):
            _, is_player_one_winner = play_game(player_one_deck[:card_one], player_two_deck[:card_two], part_two)
            if is_player_one_winner:
                player_one_deck.extend([card_one, card_two])
            else:
                player_two_deck.extend([card_two, card_one])

        elif card_one > card_two:
            player_one_deck.extend([card_one, card_two])
        else:
            player_two_deck.extend([card_two, card_one])

    return (player_one_deck, True) if player_one_deck else (player_two_deck, False)


def main():
    with open("day_22_input.txt") as f:
        input_lines = f.read().splitlines()

    player_1_deck = list()
    player_2_deck = list()
    player_1 = True
    for line in input_lines:
        if "Player" in line:
            continue
        elif not line:
            player_1 = False
        elif player_1:
            player_1_deck.append(int(line))
        else:
            player_2_deck.append(int(line))

    deck, _ = play_game(player_1_deck[:], player_2_deck[:])
    answer = sum((i + 1) * card for i, card in enumerate(reversed(deck)))
    print(f"Part 1: {answer}")

    deck, _ = play_game(player_1_deck[:], player_2_deck[:], part_two=True)
    answer = sum((i + 1) * card for i, card in enumerate(reversed(deck)))
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
