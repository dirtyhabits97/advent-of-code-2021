def main():
    f = open("input.txt", "r")
    data = parse(f)
    return calculate_risk(data)


def calculate_risk(data):

    rows, cols = len(data), len(data[0])
    risk = [[
        float("inf") if not row or not col else 0 for col in range(cols + 1)
    ] for row in range(rows + 1)]

    data[0][0] = 0
    risk[0][1] = 0

    for row in range(rows):
        for col in range(cols):
            risk[row + 1][col + 1] = min(
                risk[row + 1][col],
                risk[row][col + 1]
            ) + data[row][col]

    return risk[-1][-1]


def parse(input):
    return [list(map(int, line.strip())) for line in input]


if __name__ == '__main__':
    print(main())
