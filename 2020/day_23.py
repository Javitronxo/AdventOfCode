from collections import deque


class Cup:
    """Node for the double linked list"""
    def __init__(self, value: int):
        self.value = value
        self.previous = None
        self.next = None


def play_game_two(cups: deque, n_moves: int) -> Cup:

    # Create a double linked list keeping a separated index of cups (Similar approach as 2016/19 part 2)
    cups_index = dict()
    tail = None
    for i in cups:
        cup = Cup(i)
        cups_index[i] = cup
        if tail:
            tail.next = cup
            cup.previous = tail
        tail = cup
    head = cups_index[cups[0]]
    head.previous = tail
    tail.next = head

    current_cup = cups_index[cups[0]]
    for _ in range(n_moves):

        # Remove next three cups from the double linked list
        pick_one = current_cup.next
        pick_two = pick_one.next
        pick_three = pick_two.next
        current_cup.next = pick_three.next
        current_cup.next.previous = current_cup

        # Get the destination cup
        destination_cup_value = (current_cup.value - 1) or 1000000
        while destination_cup_value in [pick_one.value, pick_two.value, pick_three.value]:
            destination_cup_value = (destination_cup_value - 1) or 1000000
        destination_cup = cups_index[destination_cup_value]

        # Insert the three cups taking into account pick_two is already between the two cups
        pick_three.next = destination_cup.next
        pick_three.next.previous = pick_three
        destination_cup.next = pick_one
        pick_one.previous = destination_cup

        current_cup = current_cup.next

    return current_cup


def play_game_one(cups: deque, n_moves: int) -> deque:
    for _ in range(n_moves):
        current_cup_value = cups[0]
        cups.rotate(-1)
        pick_up = deque()
        for _ in range(3):
            pick_up.append(cups.popleft())

        destination_cup = None
        destination_cup_value = current_cup_value - 1
        while True:
            if destination_cup_value < min(cups):
                destination_cup_value = max(cups)
            try:
                destination_cup = cups.index(destination_cup_value)
                break
            except ValueError:
                destination_cup_value -= 1
                continue

        for i in range(3):
            cups.insert((destination_cup + i + 1) % len(cups), pick_up[i])

    return cups


def main():
    with open("day_23_input.txt") as f:
        puzzle_input = int(f.read())

    # Part 1 solved with a deque
    n_moves = 100
    cups = deque(int(char) for char in str(puzzle_input))
    cups = play_game_one(cups, n_moves)

    while cups[0] != 1:
        cups.rotate(1)
    cups.popleft()
    answer = ''.join([str(i) for i in cups])
    print(f"Part 1: {answer}")

    # Part 2 solved with a double linked list
    n_moves = 10000000
    cups = deque(int(char) for char in str(puzzle_input))
    cups.extend([max(cups) + i + 1 for i in range(1000000 - len(cups))])
    current_cup = play_game_two(cups, n_moves)

    while current_cup.value != 1:
        current_cup = current_cup.next
    answer = current_cup.next.value * current_cup.next.next.value
    print(f"Part 2: {answer}")


if __name__ == '__main__':
    main()
