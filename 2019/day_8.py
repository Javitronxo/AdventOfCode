# https://adventofcode.com/2019/day/8


def read_input_file(input_file):
    with open(input_file) as f_in:
        content = f_in.read().strip()
    return content


class Image:
    def __init__(self, digits, width, length):
        self.width = width
        self.length = length
        self.layers = self.define_layers(digits)

    def define_layers(self, digits):
        pixels_in_layer = self.width * self.length
        layers = [digits[i:i + pixels_in_layer] for i in range(0, len(digits), pixels_in_layer)]
        return layers

    def check_image_integrity(self):
        min_num_zeros, result = None, None
        for layer in self.layers:
            num_zeros = layer.count('0')
            partial_result = layer.count('1') * layer.count('2')
            if min_num_zeros is None or num_zeros < min_num_zeros:
                min_num_zeros = num_zeros
                result = partial_result
        return result

    def combine_layers(self):
        combined = '2' * len(self.layers[0])
        for layer in self.layers:
            for i in range(len(layer)):
                if combined[i] == '2':
                    if layer[i] == '0':
                        combined = combined[:i] + ' ' + combined[i + 1:]
                    else:
                        combined = combined[:i] + layer[i] + combined[i + 1:]
        final_image = [combined[i:i + self.width] for i in range(0, len(combined), self.width)]
        return final_image


def main():
    digits_str = read_input_file('day_8_input.txt')
    image = Image(digits_str, width=25, length=6)

    result_first_part = image.check_image_integrity()
    print("First part result: {}".format(result_first_part))
    result_second_part = image.combine_layers()
    print("Second part result:\n{}".format('\n'.join(result_second_part)))


if __name__ == '__main__':
    main()
