import collections
import copy
import re


def main():
    cargo_9000 = collections.defaultdict(list)
    read_instructions = False

    with open("day5_input.txt") as f:
        for line in f.readlines():
            # If we hit an empty line we start reading the move instructions
            if line.strip() == "":
                read_instructions = True
                # Post-process lists with containers and duplicate the original status for part 2
                for v in cargo_9000.values():
                    v.reverse()
                cargo_9001 = copy.deepcopy(cargo_9000)
            # Get original status of the containers
            elif not read_instructions:
                matches = re.findall(r"(\[\w]|\s{3})\s?", line)
                for i, match in enumerate(matches):
                    try:
                        letter = re.match(r"\[(\w)]", match).groups()[0]
                        cargo_9000[i + 1].append(letter)
                    except AttributeError:
                        pass
            # Move the containers according to instructions
            else:
                matches = re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0]
                containers_9000 = list()
                containers_9001 = list()
                for i in range(int(matches[0])):
                    containers_9000.append(cargo_9000[int(matches[1])].pop())
                    containers_9001.append(cargo_9001[int(matches[1])].pop())
                cargo_9000[int(matches[2])].extend(containers_9000)
                cargo_9001[int(matches[2])].extend(reversed(containers_9001))

    print(f"Part 1: {''.join([cargo_9000[i + 1][-1] for i in range(len(cargo_9000))])}")
    print(f"Part 2: {''.join([cargo_9001[i + 1][-1] for i in range(len(cargo_9001))])}")


if __name__ == "__main__":
    main()
