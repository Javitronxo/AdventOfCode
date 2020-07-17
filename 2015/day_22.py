import re


class Spell:
    def __init__(self, mana_cost: int, damage: int = 0, healing: int = 0, armor: int = 0, timer: int = 0):
        self.mana_cost = mana_cost
        self.damage = damage
        self.healing = healing
        self.armor = armor
        self.timer = timer


class MagicMissile(Spell):
    def __init__(self):
        super().__init__(mana_cost=53, damage=4)
        self.names = ["magic missile", "missile", "m"]


class Drain(Spell):
    def __init__(self):
        super().__init__(mana_cost=73, damage=2, healing=2)
        self.names = ["drain", "d"]


class Shield(Spell):
    def __init__(self):
        super().__init__(mana_cost=113, armor=7, timer=6)
        self.names = ["shield", "s"]


class Poison(Spell):
    def __init__(self):
        super().__init__(mana_cost=173, damage=3, timer=6)
        self.names = ["poison", "p"]


class Recharge(Spell):
    def __init__(self):
        super().__init__(mana_cost=229, damage=4, timer=5)
        self.mana_recharge = 101
        self.names = ["recharge", "r"]


class Character:
    def __init__(self, hit_points: int, damage: int = 0, armor: int = 0, mana: int = 0):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.mana = mana

        self.mana_used = 0
        self.active_spells = set()
        self.used_spells = list()

    def take_damage(self, damage: int):
        self.hit_points -= max(damage - self.armor, 1)

    def cast_spell(self, opponent):
        spell = None
        while not spell:
            spell_str = input("What spell do you want to cast. "
                              "Options: missile (m), drain (d), shield (s), poison (p), recharge (r): ")
            if spell_str.lower() in Shield().names:
                spell = Shield()
                self.active_spells.add(spell)
                self.armor += spell.armor
            elif spell_str.lower() in Poison().names:
                spell = Poison()
                opponent.active_spells.add(spell)
            elif spell_str.lower() in MagicMissile().names:
                spell = MagicMissile()
                opponent.take_damage(spell.damage)
            elif spell_str.lower() in Recharge().names:
                spell = Recharge()
                self.active_spells.add(spell)
            elif spell_str.lower() in Drain().names:
                spell = Drain()
                opponent.take_damage(spell.damage)
                self.hit_points += spell.healing
            else:
                print("Did not recognize the input, please use one of the valid options: "
                      "missile, drain, shield, poison, recharge")
            if spell:
                break

        self.mana -= spell.mana_cost
        self.mana_used += spell.mana_cost
        self.used_spells.append(spell.names[0])

    def apply_current_spells(self):
        spells_to_remove = set()
        for spell in self.active_spells:
            if type(spell) == Poison:
                self.take_damage(spell.damage)
                print("+ Poison damage")
            elif type(spell) == Recharge:
                self.mana += spell.mana_recharge
                print("+ Recharged mana")
            spell.timer -= 1
            if spell.timer == 0:
                spells_to_remove.add(spell)

        # Remove spells and change flags
        for spell in spells_to_remove:
            if type(spell) == Shield:
                self.armor -= spell.armor
                print("+ Armor is off now")
            elif type(spell) == Poison:
                print("+ Poison is off now")
            elif type(spell) == Recharge:
                print("+ Recharging is off now")
            self.active_spells.remove(spell)


def print_game_stats(current: Character, player: Character, boss: Character, turn: int):
    if current == player:
        current_player = 'Player'
    else:
        current_player = 'Boss'
    print(f"-- {current_player} turn #{turn} --")
    print(f"- Player has {player.hit_points} hit points, {player.armor} armor, {player.mana} mana")
    print(f"- Boss has {boss.hit_points} hit points")
    print(f"* Player has spent {player.mana_used} mana so far")


def play_game(player: Character, boss: Character, hard_level: bool = False) -> bool:
    """Play the game with current character set
    NOTE: THIS IS AN INTERACTIVE GAME

    Return True if player wins, False otherwise
    """
    current = player
    turn = 0
    while player.hit_points > 0 and boss.hit_points > 0:
        # Play it the hard mode
        if hard_level and current == player and turn != 0:
            player.take_damage(1)
            if player.hit_points <= 0:
                return False

        # Print stats and apply existing conditions
        boss.apply_current_spells()
        player.apply_current_spells()
        print_game_stats(current, player, boss, turn)
        if player.hit_points <= 0 or boss.hit_points <= 0:
            break

        # Play the turn
        if current == player:
            player.cast_spell(boss)
            if player.mana <= 0:
                return False
        else:
            player.take_damage(boss.damage)

        current = player if current == boss else boss
        print()
        turn += 1

    return True if boss.hit_points <= 0 else False


def print_game_summary(player: Character, winner: bool):
    if not winner:
        print(f"You are a loser! We spent {player.mana_used} mana in this battle and lost!")
    else:
        print(f"We won! We spent {player.mana_used} mana in this battle. Spells used: {' -> '.join(player.used_spells)}")


def main():
    # Initialize the characters
    with open('day_22_input.txt') as f_in:
        input_str = f_in.read()
        boss_stats = re.findall(r'\d+', input_str)
        boss = Character(hit_points=int(boss_stats[0]), damage=int(boss_stats[1]))
    player = Character(hit_points=50, mana=500)

    # Part 1: Easy mode
    winner = play_game(player, boss)
    print_game_summary(player, winner)
    # Wining combo:
    # Magic Missile -> Poison -> Recharge -> Magic Missile -> Poison -> Shield -> Magic Missile -> Magic Missile

    # # Part 2: hard mode
    winner = play_game(player, boss, hard_level=True)
    print_game_summary(player, winner)
    # Wining combo: Poison -> Magic Missile -> Recharge -> Poison -> Shield -> Recharge -> Poison -> Drain


if __name__ == '__main__':
    main()
