def main():
    f = open("input.txt", "r")
    data = parse(f)

    rows, cols = number_of_rows(data), number_of_cols(data)

    board = [[0 for _ in range(cols)] for _ in range(rows)]

    for start, end in data:
        mark(board, start, end)

    return count_overlap(board)


# TODO: implement this
def parse(raw_data):
    """
    Output format:
    [
        [start_col, start_row, end_col, end_row],
        ...
    ]
    """
    ans = []

    for line in raw_data:
        start, end = line.split("->")
        start_col, start_row = start.split(",")
        end_col, end_row = end.split(",")

        ans.append([
            int(start_col), int(start_row), int(end_col), int(end_row)
        ])

    return ans


def number_of_rows(data):
    """
    Input format:
    [
        [start_col, start_row, end_col, end_row],
        ...
    ]

    We compare every row's idx=1,3 elements.
    """
    ans = 0

    for row in data:
        ans = max(ans, row[1], row[3])

    return ans


def number_of_cols(data):
    """
    Input format:
    [
        [start_col, start_row, end_col, end_row],
        ...
    ]

    We compare every row's idx=0,2 elements.
    """
    ans = 0

    for row in data:
        ans = max(ans, row[0], row[2])

    return ans


def count_overlap(board):
    count = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] > 1:
                count += 1

    return 0


def mark(board, start, end):
    # If same col, mark every row
    if start[0] == end[0]:
        # get the bounds
        lo, hi = start[1], end[1]
        if lo > hi:
            lo, hi = hi, lo

        for row in range(lo, hi+1):
            board[row][start[0]] += 1

    # If same row, mark every column
    elif start[1] == end[1]:
        lo, hi = start[0], end[0]
        if lo > hi:
            lo, hi = hi, lo

        for col in range(lo, hi+1):
            board[start[1]][col] += 1


if __name__ == '__main__':
    print(main())
