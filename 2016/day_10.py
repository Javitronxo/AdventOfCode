import re


class Node:
    def __init__(self, number: str):
        self.number = number
        self.chips = list()

    def add_chip(self, value: str):
        self.chips.append(int(value))


class Bot(Node):
    TARGET_CHIPS = [17, 61]

    def __init__(self, number: str):
        super(Bot, self).__init__(number=number)
        self.low = None
        self.high = None

    def add_chip(self, value: str):
        self.chips.append(int(value))
        if len(self.chips) == 2:
            if sorted(self.chips) == self.TARGET_CHIPS:
                print(f"Part 1: Bot {self.number} got chips {self.TARGET_CHIPS}")
            low_chip, high_chip = sorted(self.chips)
            self.low.add_chip(low_chip)
            self.high.add_chip(high_chip)
            self.chips.clear()


def main():
    bot_pattern = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'
    input_pattern = r'value (\d+) goes to bot (\d+)'

    bots = list()
    outputs = list()
    with open('day_10_input.txt') as f_in:
        lines = f_in.readlines()

        # Initialize all bots
        for line in lines:
            if re.search(bot_pattern, line):
                bot_info = re.search(bot_pattern, line).groups()
                bot = Bot(bot_info[0])
                # Define low value
                if bot_info[1] == 'output':
                    output = Node(bot_info[2])
                    bot.low = output
                    outputs.append(output)
                else:
                    bot.low = bot_info[2]
                # Define high value
                if bot_info[3] == 'output':
                    output = Node(bot_info[4])
                    bot.high = output
                    outputs.append(output)
                else:
                    bot.high = bot_info[4]
                bots.append(bot)

        # Build graph: Replace node values with Bot objects
        for bot in bots:
            if isinstance(bot.low, str):
                bot.low = [target_bot for target_bot in bots if target_bot.number == bot.low][0]
            if isinstance(bot.high, str):
                bot.high = [target_bot for target_bot in bots if target_bot.number == bot.high][0]

        # Distribute the chips
        for line in lines:
            if re.search(input_pattern, line):
                input_info = re.search(input_pattern, line).groups()
                bot = [target_bot for target_bot in bots if target_bot.number == input_info[1]][0]
                bot.add_chip(input_info[0])

    part_2_result = 1
    for output in outputs:
        if output.number in ['0', '1', '2']:
            part_2_result *= output.chips[0]
    print(f"Part 2: Multiply together the values of one chip in each of outputs 0, 1, and 2: {part_2_result}")


if __name__ == '__main__':
    main()
