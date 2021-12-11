def main():
    f = open("demo.txt", "r")
    f = open("input.txt", "r")
    data = parse(f)

    steps = 100
    ans = 0
    for _ in range(steps):
        flash(data)
        ans += correct(data)
    return ans


def parse(input):
    data = []
    for line in input:
        row = []
        for char in line.strip():
            row.append(int(char))
        data.append(row)

    for row in data:
        print(row)
    return data


def flash(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            flash_item(matrix, row, col)


def flash_item(matrix, row, col):
    matrix[row][col] += 1
    # if the element == 10, we need to flash the neighbors
    if matrix[row][col] != 10:
        return
    rows, cols = len(matrix), len(matrix[0])
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = row+dx, col+dy
        # check within bounds
        if x < 0 or x >= rows or y < 0 or y >= cols:
            continue
        flash_item(matrix, x, y)


def correct(matrix):
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 9:
                ans += 1
                matrix[row][col] = 0
    return ans


if __name__ == '__main__':
    print(main())
