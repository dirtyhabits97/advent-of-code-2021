from collections import defaultdict


def main():
    f = open("input.txt", "r")
    data = parse(f)
    return count_paths(data)


def count_paths(data):
    return visit(data, 'start', set())


def visit(data, node, visited):
    # if reached the end, return 1
    if node == 'end':
        return 1
    # mark as visited if lower case
    if node.islower():
        visited.add(node)

    ans = 0
    for neighbor in data[node]:
        # if the neighbor is already visited, skip it
        if neighbor in visited:
            continue
        ans += visit(data, neighbor, visited)

    if node in visited:
        visited.remove(node)

    return ans


def parse(input):
    data = defaultdict(lambda: [])
    for line in input:
        lhs, rhs = line.split("-")
        data[lhs].append(rhs.strip())
        data[rhs.strip()].append(lhs)
    return data


if __name__ == '__main__':
    print(main())
