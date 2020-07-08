import re


class Sue:
    def __init__(self, number: int, properties: dict):
        self.number = number
        self.properties = properties

    def match_properties_inaccurate(self, target_properties: dict) -> bool:
        return all(value == target_properties[key] for key, value in self.properties.items())

    def match_properties(self, target_properties: dict) -> bool:
        for key, value in self.properties.items():
            if (key in ['cats', 'trees'] and value <= target_properties[key]) or \
                    (key in ['pomeranians', 'goldfish'] and value >= target_properties[key]) or \
                    (key not in ['cats', 'trees', 'pomeranians', 'goldfish'] and value != target_properties[key]):
                return False
        return True


def main():
    line_pattern = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    with open('day_16_input.txt') as f_in:
        sues = list()
        for line in f_in.readlines():
            sue_signature = re.findall(line_pattern, line)[0]
            number = int(sue_signature[0])
            properties = dict()
            for i in range(1, len(sue_signature), 2):
                properties[sue_signature[i]] = int(sue_signature[i + 1])
            sue = Sue(number, properties)
            sues.append(sue)

    target_properties = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    for sue in sues:
        if sue.match_properties_inaccurate(target_properties):
            print('The inaccurate Sue is: %d' % sue.number)
        if sue.match_properties(target_properties):
            print('The real Sue is: %d' % sue.number)


if __name__ == '__main__':
    main()
