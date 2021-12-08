def main():
    f = open("input.txt", "r")
    # f = open("demo.txt", "r")
    data = parse(f)

    return find_occurrence(data)


def parse(input):
    data = []
    for line in input:
        patterns, output = line.split("|")
        patterns, output = patterns.split(), output.split()
        data.append([patterns, output])
    return data


def find_occurrence(data):
    """
    Expected input:
    [
        # [signals], [output]
        ['be', 'cfbegad', ...], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'],
        ...
    ]
    For this first puzzle, to find occurrences of 1, 4, 7 and 8 we count
    the str length.
    1 -> 2 chars to represent
    4 -> 4 chars to represent
    7 -> 3 chars to represent
    8 -> 7 chars to represent
    """
    ans = 0
    for _, outputs in data:
        for output in outputs:
            if len(output) == 2:
                ans += 1
            elif len(output) == 4:
                ans += 1
            elif len(output) == 3:
                ans += 1
            elif len(output) == 7:
                ans += 1
    return ans


if __name__ == '__main__':
    print(main())
