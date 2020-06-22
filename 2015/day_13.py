import re
from collections import defaultdict
from itertools import permutations


class Person:
    def __init__(self, name):
        self.name = name
        self.happiness_map = defaultdict(int)

    def define_happiness(self, person_name, happiness):
        self.happiness_map[person_name] = happiness


def get_maximum_happiness(people: list) -> int:
    maximum_happiness = -1
    for people_arrange in permutations(people):
        happiness_delta = 0
        for i in range(len(people_arrange)):
            happiness_delta += people_arrange[i].happiness_map[people_arrange[(i + 1) % len(people_arrange)].name] + \
                               people_arrange[i].happiness_map[people_arrange[(i - 1) % len(people_arrange)].name]
        if happiness_delta > maximum_happiness:
            maximum_happiness = happiness_delta
    return maximum_happiness


def main():
    line_pattern = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'
    people = list()

    with open('day_13_input.txt') as f_in:
        for line in f_in.readlines():
            person_1, outcome, quantity, person_2 = re.findall(line_pattern, line)[0]
            if person_1 not in [person.name for person in people]:
                person = Person(person_1)
                people.append(person)
            else:
                person = [person for person in people if person.name == person_1][0]
            happiness = -int(quantity) if outcome == 'lose' else int(quantity)
            person.define_happiness(person_2, happiness)

    maximum_happiness = get_maximum_happiness(people)
    print('Total change in happiness for the optimal seating arrangement is %d' % maximum_happiness)

    people.append(Person('Javitronxo'))
    maximum_happiness = get_maximum_happiness(people)
    print('Total change in happiness for the optimal seating arrangement with myself is %d' % maximum_happiness)


if __name__ == '__main__':
    main()
