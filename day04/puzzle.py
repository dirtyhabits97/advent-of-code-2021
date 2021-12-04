
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
    for row in rows:
        for col in cols:
            if not board[row][col][1]:
                break
        return True

    # 2. check cols
    for col in cols:
        for row in rows:
            if not board[row][col][1]:
                break
        return True
