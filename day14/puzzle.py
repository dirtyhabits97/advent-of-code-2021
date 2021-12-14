from collections import Counter


def main():
    f = open("input.txt", "r")
    sequence, templates = parse(f)
    sequence = expand(sequence, templates, 10)
    return count(sequence)


def count(sequence):
    counter = Counter(sequence).most_common()
    max, min = counter[0][1], counter[-1][1]
    return max - min


def expand(sequence, templates, steps):
    print(sequence)

    for step in range(steps):
        new_seq = []
        for idx in range(len(sequence) - 1):
            new_seq.append(sequence[idx])
            pair = "".join([sequence[idx], sequence[idx+1]])
            new_seq.append(templates[pair])

        new_seq.append(sequence[-1])
        sequence = new_seq
        print(step + 1, len(sequence))

    return sequence


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
