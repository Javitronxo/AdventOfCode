
def read_file_to_int_list(file_name):
    with open(file_name) as f_in:
        input_list = [int(x) for x in f_in.read().split(',')]
    return input_list
