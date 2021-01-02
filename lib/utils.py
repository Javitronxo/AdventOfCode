from collections import defaultdict
from hashlib import md5
from math import gcd


def read_file_to_int_list(file_name):
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(",")]
    return input_list


def read_file_to_int_dict(file_name):
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(",")]
    input_dict = defaultdict(int)
    for i in range(len(input_list)):
        input_dict[i] = int(input_list[i])
    return input_dict


def lcm(x, y):
    """This function computes LCM"""
    return (x * y) // gcd(x, y)


def get_md5_hash(input_str: str) -> str:
    return md5(bytes(input_str, encoding="utf-8")).hexdigest()
