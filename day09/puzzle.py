def main():
    f = open("input.txt", "r")
    # f = open("demo.txt", "r")
    data = parse(f)
    return low_points_sum(data)


def parse(input):
    ans = []
    for line in input:
        row = []
        # skip the '\n char'
        for char in line[:-1]:
            row.append(int(char))
        ans.append(row)
    return ans


def low_points_sum(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if is_low_point(matrix, row, col):
                # riks level = height + 1
                sum += matrix[row][col] + 1
    return sum


def is_low_point(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = row+dx, col+dy

        # validate bounds
        if x < 0 or x >= rows or y < 0 or y >= cols:
            continue

        if matrix[row][col] >= matrix[x][y]:
            return False

    return True


if __name__ == '__main__':
    print(main())
