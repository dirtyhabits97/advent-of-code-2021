from collections import defaultdict


def main():
    f = open("input.txt", "r")
    data = parse(f)
    return count_paths(data)


def count_paths(data):
    return visit(data, 'start', set(), True)


def visit(graph, node, visited, bonusVisit):
    if node == 'end':
        return 1

    if node in visited:
        if not bonusVisit or node == 'start':
            return 0
        bonusVisit = False

    v = visited if node[0].isupper() else visited | set([node])
    return sum(visit(graph, next, v, bonusVisit) for next in graph[node])


def parse(input):
    data = defaultdict(lambda: [])
    for line in input:
        lhs, rhs = line.split("-")
        data[lhs].append(rhs.strip())
        data[rhs.strip()].append(lhs)
    return data


if __name__ == '__main__':
    print(main())
