from collections import defaultdict
from hashlib import md5
from math import gcd
from typing import Dict, List


def read_file_to_int_list(file_name: str) -> List[int]:
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(",")]
    return input_list


def read_file_to_int_dict(file_name: str) -> Dict[int, int]:
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(",")]
    input_dict = defaultdict(int)
    for i in range(len(input_list)):
        input_dict[i] = int(input_list[i])
    return input_dict


def lcm(input_list: List[int]):
    """This function computes LCM"""
    value = 1
    for i in input_list:
        value = value * i // gcd(value, i)
    return value


def get_md5_hash(input_string: str, stretch_factor: int = None) -> str:
    """Get MD5 hexadecimal hash"""
    hex_hash = md5(bytes(input_string, "utf-8")).hexdigest()
    if stretch_factor:
        for _ in range(stretch_factor):
            hex_hash = get_md5_hash(hex_hash)
    return hex_hash
