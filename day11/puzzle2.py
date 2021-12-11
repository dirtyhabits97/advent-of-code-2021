def main():
    f = open("demo.txt", "r")
    f = open("input.txt", "r")
    data = parse(f)
    log(data, "before")

    step = 1
    while True:
        flash(data)
        if correct(data):
            log(data, "after")
            return step

        step += 1


def log(matrix, title):
    print("========== ", title, " ==========")
    for row in matrix:
        print(row)
    print("==============================")


def parse(input):
    data = []
    for line in input:
        row = []
        for char in line.strip():
            row.append(int(char))
        data.append(row)

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
    all_above_9 = True
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 9:
                matrix[row][col] = 0
            else:
                all_above_9 = False
    return all_above_9


if __name__ == '__main__':
    print(main())
