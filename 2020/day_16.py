import re
from collections import defaultdict


def main():
    ticket_fields = dict()
    tickets = list()
    with open("day_16_input.txt") as f:
        i = 0
        for line in f.read().splitlines():
            if not len(line):
                i += 1
                continue
            elif "ticket" in line:
                continue

            if i == 0:
                field, values = line.split(": ")
                range_values = re.findall(r"(\d+)-(\d+) or (\d+)-(\d+)", values)[0]
                ticket_fields[field] = [int(x) for x in range_values]
            elif i == 1:
                my_ticket = [int(x) for x in line.split(",")]
            elif i == 2:
                tickets.append([int(x) for x in line.split(",")])

    valid_tickets = list()
    invalid_numbers = list()
    for ticket in tickets:
        valid_ticket = True
        for number in ticket:
            valid_number = False
            for field, values in ticket_fields.items():
                if values[0] <= number <= values[1] or values[2] <= number <= values[3]:
                    valid_number = True
            if not valid_number:
                valid_ticket = False
                invalid_numbers.append(number)
        if valid_ticket:
            valid_tickets.append(ticket)
    print(f"Part 1: {sum(invalid_numbers)}")

    valid_ticket_order = defaultdict(set)
    invalid_ticket_order = defaultdict(set)
    for ticket in valid_tickets:
        for i, number in enumerate(ticket):
            for field, values in ticket_fields.items():
                if values[0] <= number <= values[1] or values[2] <= number <= values[3]:
                    valid_ticket_order[i].add(field)
                else:
                    invalid_ticket_order[i].add(field)

    for i in range(len(valid_ticket_order)):
        valid_ticket_order[i] = valid_ticket_order[i].difference(invalid_ticket_order[i])

    while not all(len(x) == 1 for x in valid_ticket_order.values()):
        for i in range(len(valid_ticket_order)):
            if len(valid_ticket_order[i]) == 1:
                for j in range(len(valid_ticket_order)):
                    if i == j or len(valid_ticket_order[j]) == 1:
                        continue
                    try:
                        valid_ticket_order[j].remove(list(valid_ticket_order[i])[0])
                    except KeyError:
                        pass

    target_classes = "departure"
    answer = 1
    for number, field in zip(my_ticket, valid_ticket_order.values()):
        if list(field)[0].startswith(target_classes):
            answer *= number

    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
