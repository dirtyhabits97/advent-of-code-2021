def main():
    f = open("input.txt", "r")
    coordinates, folds = parse(f)
    matrix = build_matrix(coordinates)
    fill(matrix, coordinates)
    fold(matrix, folds)
    log(matrix)


def log(matrix):
    for row in range(7):
        print("".join(matrix[row]))


def count_folds(matrix):
    ans = 0
    for row in matrix:
        for char in row:
            ans += 1 if char == '#' else 0
    return ans


def fold(matrix, folds):
    for axis, value in folds:
        if axis == 'x':
            fold_x(matrix, value)
        else:
            fold_y(matrix, value)


def fold_x(matrix, value):
    for row in range(len(matrix)):
        lhs = r = value
        lend, rend = 0, len(matrix[0]) - 1

        while lhs >= lend and r <= rend:
            if matrix[row][r] == '#':
                matrix[row][lhs] = '#'
            r += 1
            lhs -= 1

        for col in range(value + 1, rend + 1):
            matrix[row][col] = '.'


def fold_y(matrix, value):
    top = bot = value
    tend, bend = 0, len(matrix) - 1

    while top >= tend and bot <= bend:
        for col in range(len(matrix[top])):
            if matrix[bot][col] == '#':
                matrix[top][col] = '#'
        top -= 1
        bot += 1

    for row in range(value + 1, bend + 1):
        for col in range(len(matrix[row])):
            matrix[row][col] = '.'


def fill(matrix, coordinates):
    for col, row in coordinates:
        matrix[row][col] = '#'


def build_matrix(coordinates):
    rows = max(coordinates, key=lambda c: c[1])[1] + 1
    cols = max(coordinates, key=lambda c: c[0])[0] + 1
    print("rows: %d, cols: %d" % (rows, cols))
    return [['.' for _ in range(cols)] for _ in range(rows)]


def parse(input):
    """
    Coordinates:
    [
        (col, row), ...
    ]

    Folds:
    [
        (axis, value), ...
    ]
    """
    coordinates, folds = [], []
    readCoordinates = True
    for line in input:
        line = line.strip()

        if not line:
            readCoordinates = False
            continue

        if readCoordinates:
            coordinates.append(tuple(map(int, line.strip().split(","))))
        else:
            line = line.replace("fold along ", "")
            axis, value = line.split("=")
            folds.append((axis, int(value)))
    return coordinates, folds


if __name__ == '__main__':
    print(main())
