import itertools
import re
from sys import maxsize

ITEMS = {
    'Weapons': {
        'Dagger': {
            'cost': 8, 'damage': 4, 'armor': 0,
        },
        'Shortsword': {
            'cost': 10, 'damage': 5, 'armor': 0,
        },
        'Warhammer': {
            'cost': 25, 'damage': 6, 'armor': 0,
        },
        'Longsword': {
            'cost': 40, 'damage': 7, 'armor': 0,
        },
        'Greataxe': {
            'cost': 74, 'damage': 8, 'armor': 0,
        },
    },
    'Armor': {
        'None': {
            'cost': 0, 'damage': 0, 'armor': 0,
        },
        'Leather': {
            'cost': 13, 'damage': 0, 'armor': 1,
        },
        'Chainmail': {
            'cost': 31, 'damage': 0, 'armor': 2,
        },
        'Splintmail': {
            'cost': 53, 'damage': 0, 'armor': 3,
        },
        'Bandedmail': {
            'cost': 75, 'damage': 0, 'armor': 4,
        },
        'Platemail': {
            'cost': 102, 'damage': 0, 'armor': 5,
        },
    },
    'Rings': {
        'None 1': {
            'cost': 0, 'damage': 0, 'armor': 0,
        },
        'None 2': {
            'cost': 0, 'damage': 0, 'armor': 0,
        },
        'Damage +1': {
            'cost': 25, 'damage': 1, 'armor': 0,
        },
        'Damage +2': {
            'cost': 50, 'damage': 2, 'armor': 0,
        },
        'Damage +3': {
            'cost': 100, 'damage': 3, 'armor': 0,
        },
        'Defense +1': {
            'cost': 20, 'damage': 0, 'armor': 1,
        },
        'Defense +2': {
            'cost': 40, 'damage': 0, 'armor': 2,
        },
        'Defense +3': {
            'cost': 80, 'damage': 0, 'armor': 3,
        },
    },
}


class Character:
    def __init__(self, hit_points: int, damage: int = 0, armor: int = 0):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage: int):
        self.hit_points -= max(damage - self.armor, 1)

    def add_items(self, items: list):
        for item in items:
            self.damage += item['damage']
            self.armor += item['armor']


def play_game(player: Character, boss: Character) -> bool:
    """Play the game with current character set
    Return True if player wins, False otherwise
    """
    attacker = player
    defender = boss
    while player.hit_points > 0 and boss.hit_points > 0:
        defender.take_damage(attacker.damage)
        attacker, defender = defender, attacker
    return True if boss.hit_points <= 0 else False


def main():
    # Initialize the characters
    with open('day_21_input.txt') as f_in:
        input_str = f_in.read()
        boss_stats = re.findall(r'\d+', input_str)
        boss = Character(hit_points=int(boss_stats[0]), damage=int(boss_stats[1]), armor=int(boss_stats[2]))
    player = Character(hit_points=100)

    # You must buy exactly one weapon; no dual-wielding.
    weapons = ITEMS['Weapons']
    # Armor is optional, but you can't use more than one.
    armor = ITEMS['Armor']
    # You can buy 0-2 rings. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.
    rings = ITEMS['Rings']
    rings_combinations = itertools.combinations(rings, r=2)

    min_cost = maxsize
    max_cost = 0
    for weapon, armor, rings in itertools.product(weapons, armor, rings_combinations):
        # Set up the character
        items = [ITEMS['Weapons'][weapon], ITEMS['Armor'][armor], ITEMS['Rings'][rings[0]], ITEMS['Rings'][rings[1]]]
        player.add_items(items)
        total_cost = sum([item['cost'] for item in items])

        # Play the simulation
        winner = play_game(player, boss)
        if winner:
            min_cost = min(min_cost, total_cost)
        elif not winner:
            max_cost = max(max_cost, total_cost)

        # Reset the players
        player = Character(hit_points=100)
        boss = Character(hit_points=int(boss_stats[0]), damage=int(boss_stats[1]), armor=int(boss_stats[2]))

    print(f"Part 1: We can win the game with at least {min_cost} pieces of gold")
    print(f"Part 2: We can spend maximum {max_cost} pieces of gold and still lose")


if __name__ == '__main__':
    main()
