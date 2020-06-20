def get_ribbon(length: int, width: int, height: int) -> int:
    dimensions = [length, width, height]
    dimensions.sort()
    return sum(dimensions[:2]) * 2 + (length * width * height)


def get_gift_paper(length: int, width: int, height: int) -> int:
    return 2 * (length * width + length * height + width * height) + \
           min([length * width, length * height, width * height])


def main():
    paper_needed = 0
    ribbon_needed = 0
    with open('day_2_input.txt') as f_in:
        for line in f_in.readlines():
            length, width, height = line.split('x')
            paper_needed += get_gift_paper(int(length), int(width), int(height))
            ribbon_needed += get_ribbon(int(length), int(width), int(height))
    print('The elves need %d sqft of paper' % paper_needed)
    print('The elves need %d ft of ribbon' % ribbon_needed)


if __name__ == '__main__':
    main()
