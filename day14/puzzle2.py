from collections import defaultdict


def main():
    f = open("input.txt", "r")
    sequence, templates = parse(f)
    return count(expand(sequence, templates, 40))


def count(grouped):
    print(grouped)
    return max(grouped.values()) - min(grouped.values())


def expand(sequence, templates, steps):
    grouped = defaultdict(lambda: 0)
    for idx in range(len(sequence) - 1):
        grouped[sequence[idx]+sequence[idx+1]] += 1

    for _ in range(steps):
        new_groups = defaultdict(lambda: 0)
        for pair in grouped:
            # pair -> HP; template: HP -> T
            # pair[0] + templates[pair] = HT
            new_groups[pair[0] + templates[pair]] += grouped[pair]
            # templates[pair] + pair[1] = TP
            new_groups[templates[pair] + pair[1]] += grouped[pair]
        grouped = new_groups

    # split every pair by character
    # e.g. SF -> 'S'
    ans = defaultdict(lambda: 0)
    for pair in grouped:
        ans[pair[0]] += grouped[pair]
    # the last character alwasy has an extra count
    ans[sequence[-1]] += 1

    return ans


def parse(input):
    lines = input.readlines()
    sequence = [char for char in lines[0].strip()]
    templates = {}
    for line in lines[2:]:
        lhs, rhs = line.strip().split(" -> ")
        templates[lhs] = rhs
    return sequence, templates


if __name__ == '__main__':
    print(main())
