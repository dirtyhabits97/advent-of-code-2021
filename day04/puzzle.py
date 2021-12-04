def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    nums = parse_nums(lines[:1])
    boards = parse_boards(lines[2:])

    return bingo(nums, boards)


def parse_nums(input):
    nums = list(map(int, input[0].split(",")))
    return nums


def parse_boards(input):
    boards = []
    buffer = []
    for line in input:

        if line == "\n":
            boards.append(buffer)
            buffer = []

        else:
            row = []
            for num in line.split():
                row.append([int(num), False])
            buffer.append(row)

    return boards


def bingo(nums, boards):
    for num in nums:
        for board in boards:
            mark(num, board)

            if check_if_won(board):
                print("board won", board, score(board), num)
                return score(board) * num

    return -1


def score(board):
    rows, cols = len(board), len(board[0])
    ans = 0

    for row in range(rows):
        for col in range(cols):
            if not board[row][col][1]:
                ans += board[row][col][0]

    return ans


def mark(num, board):
    """
    Marks a number in the board if it exists.

    This could be optimized if we keep track of the indices
    in a dictionary (O(1)).
    """

    rows, cols = len(board), len(board[0])

    for row in range(rows):
        for col in range(cols):
            if num == board[row][col][0]:
                board[row][col][1] = True


def check_if_won(board):
    """
    Checks if the board has a full row or column.

    Example input:
    [
        [(20, True), (13, False), (15, False)],
        [(21, True), (14, False), (18, False)],
        [(22, True), (33, False), (57, False)],
    ]
    """

    rows, cols = len(board), len(board[0])

    # 1. check rows
    for row in range(rows):
        all_true = True
        for col in range(cols):
            if not board[row][col][1]:
                all_true = False
                break

        if all_true:
            return True

    # 2. check cols
    for col in range(cols):
        all_true = True
        for row in range(rows):
            if not board[row][col][1]:
                all_true = False
                break
        if all_true:
            return True

    return False


if __name__ == '__main__':
    print(main())
