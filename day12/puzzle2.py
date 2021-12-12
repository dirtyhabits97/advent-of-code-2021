from collections import defaultdict


def main():
    f = open("input.txt", "r")
    data = parse(f)
    return count_paths(data)


def count_paths(data):
    return visit(data, 'start', set(), ['start'], False, False)


def visit(graph, node, visited, stack, ignoreCurrentNode, alreadyIgnored):
    if node == 'end':
        # This is not an optimal solution
        # should cache the visited edges in a matrix for faster lookup
        hashed = tuple(stack)
        if hashed in visited:
            return 0
        else:
            visited.add(hashed)
            print(stack)
            return 1

    if not ignoreCurrentNode:
        visited.add(node)

    ans = 0
    for neighbor in graph[node]:
        if neighbor in visited:
            continue

        # check if is a big cave
        if neighbor.isupper():
            ans += visit(graph, neighbor, visited, stack + [neighbor], True, alreadyIgnored)
            continue

        # handle small cave
        # 1. if we already visited a small cave twice, visit the rest only once
        if alreadyIgnored:
            ans += visit(graph, neighbor, visited, stack + [neighbor], False, True)
            continue
        # 2. if we havent visited a small case twice:
        # a. visit all the caves once
        ans += visit(graph, neighbor, visited, stack + [neighbor], False, False)
        # b. visit the current neighbor twice
        ans += visit(graph, neighbor, visited, stack + [neighbor], True, True)

    if node in visited:
        visited.remove(node)

    return ans


def parse(input):
    data = defaultdict(lambda: [])
    for line in input:
        lhs, rhs = line.split("-")
        data[lhs].append(rhs.strip())
        # exclude 'start' as a viable neighbor
        if lhs != 'start':
            data[rhs.strip()].append(lhs)
    return data


if __name__ == '__main__':
    print(main())
