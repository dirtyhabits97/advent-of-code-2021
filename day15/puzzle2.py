from queue import PriorityQueue


def main():
    f = open("input.txt", "r")
    data = parse(f)
    return calculate_risk(expand(data))


def expand(data):
    col, cols = 0, len(data[0])

    # expand to the right
    for _ in range(4 * cols):
        for row in range(len(data)):
            new = data[row][col] + 1
            new = new if new <= 9 else 1
            data[row].append(new)
        col += 1
    # expand below
    row, rows = 0, len(data)
    for _ in range(4 * rows):
        data.append([])
        for col in range(len(data[row])):
            new = data[row][col] + 1
            new = new if new <= 9 else 1
            data[-1].append(new)
        row += 1

    return data


def calculate_risk(data):
    # Use Dijkstra
    rows, cols = len(data), len(data[0])
    risk = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    # priority queue
    q = PriorityQueue()
    q.put((0, 0, 0))

    while not q.empty():
        weight, row, col = q.get()
        # if we've calculated a cheaper path, skip computation
        if weight > risk[row][col]:
            continue
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x, y = row+dx, col+dy
            # check within bounds
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue
            # calculate new weight for path / edge
            new_weight = weight + data[x][y]
            # check if we haven't seen a cheaper path
            if new_weight < risk[x][y]:
                risk[x][y] = new_weight
                q.put((new_weight, x, y))

    return risk[-1][-1]


def parse(input):
    return [list(map(int, line.strip())) for line in input]


if __name__ == '__main__':
    print(main())
