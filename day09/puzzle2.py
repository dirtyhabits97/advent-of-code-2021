from math import prod

def main():
    f = open("input.txt", "r")
    # f = open("demo.txt", "r")
    data = parse(f)
    return basins_score(data)


def parse(input):
    ans = []
    for line in input:
        row = []
        # skip the '\n char'
        for char in line[:-1]:
            row.append(int(char))
        ans.append(row)
    return ans


def basins_score(matrix):
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # '9's don't count
            if matrix[row][col] == 9:
                continue
            # '-1' are visited elements
            if matrix[row][col] == -1:
                continue

            sizes.append(basin_size(matrix, row, col))

    return prod(sorted(sizes)[-3:])


def basin_size(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])

    matrix[row][col] = -1
    ans = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = row+dx, col+dy
        # validate bounds
        if x < 0 or x >= rows or y < 0 or y >= cols:
            continue
        # validate it can be visited
        if matrix[x][y] == 9 or matrix[x][y] == -1:
            continue
        ans += basin_size(matrix, x, y)

    return ans


if __name__ == '__main__':
    print(main())
