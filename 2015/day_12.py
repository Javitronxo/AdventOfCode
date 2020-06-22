import json
from typing import Union, Any


def get_sum_list_elements(element: Any, ignore: str = None) -> int:
    total_sum = 0
    if isinstance(element, list) or \
            (isinstance(element, dict) and ignore not in (list(element.keys()) + list(element.values()))):
        total_sum += get_sum_elements(element, ignore)
    elif isinstance(element, int):
        total_sum += element
    return total_sum


def get_sum_elements(input_json: Union[list, dict], ignore: str = None) -> int:
    total_sum = 0
    if isinstance(input_json, list):
        for element in input_json:
            total_sum += get_sum_list_elements(element, ignore)
    elif isinstance(input_json, dict):
        for key, element in input_json.items():
            if isinstance(key, int):
                total_sum += key
            total_sum += get_sum_list_elements(element, ignore)
    return total_sum


def main():
    input_json = json.load(open('day_12_input.txt'))
    print('Sum of all the numbers is %s' % get_sum_elements(input_json))
    print('Sum of all the numbers without red is %s' % get_sum_elements(input_json, 'red'))


if __name__ == '__main__':
    main()
