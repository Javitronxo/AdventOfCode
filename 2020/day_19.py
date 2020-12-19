import re
from typing import Dict


def expand_rules(rules: Dict[str, str], expanded_rules: Dict[str, str]) -> Dict[str, str]:
    """Apply original rules to new set of expanded expression. Function intended for a while loop."""
    for number, expression in rules.items():
        if expression.startswith('"'):
            expanded_rules[number] = expression.replace('"', "")
        else:
            parts = expression.split()
            if all(part in expanded_rules.keys() for part in parts if part != "|"):
                expanded_rule = str()
                for part in parts:
                    expanded_rule += "|" if part == "|" else expanded_rules[part]
                expanded_rules[number] = f"({expanded_rule})"
    return expanded_rules


def main():
    rules = {}
    messages = list()
    with open("day_19_input.txt") as f:
        input_lines = f.read().splitlines()
        is_rule = True
        for line in input_lines:
            if not line:
                is_rule = False
            elif is_rule:
                rule_number, rule_expression = line.split(": ")
                rules[rule_number] = rule_expression
            else:
                messages.append(line)

    expanded_rules = dict()
    while len(expanded_rules) != len(rules):
        expanded_rules = expand_rules(rules, expanded_rules)
    print(f"Part 1: {len([message for message in messages if re.fullmatch(expanded_rules['0'], message)])}")

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    matched_messages = set()
    while True:
        expanded_rules = expand_rules(rules, expanded_rules)
        new_matched_messages = {
            message
            for message in messages
            if re.fullmatch(expanded_rules["0"], message) and message not in matched_messages
        }
        if not new_matched_messages:
            break
        matched_messages.update(new_matched_messages)
    print(f"Part 2: {len(matched_messages)}")


if __name__ == "__main__":
    main()
