def main():
    f = open("demo.txt", "r")
    coordinates, folds = parse(f)
    matrix = build_matrix(coordinates)
    fill(matrix, coordinates)
    fold(matrix, folds)
    return count_folds(matrix)

def count_folds(matrix):
    ans = 0
    for row in matrix:
        for char in row:
            ans += 1 if char == '#' else 0
        print(row)
    return ans


def fold(matrix, folds):
    pass


def fill(matrix, coordinates):
    for col, row in coordinates:
        matrix[row][col] = '#'


def build_matrix(coordinates):
    rows = max(coordinates, key=lambda c: c[1])[1] + 1
    cols = max(coordinates, key=lambda c: c[0])[0] + 1
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
