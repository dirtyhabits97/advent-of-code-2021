def main():
    f = open("input.txt", "r")
    f = open("demo.txt", "r")
    data = parse(f)

    for row in data:
        print(row)

    return []


def parse(input):
    data = []
    for line in input:
        patterns, output = line.split("|")
        patterns, output = patterns.split(), output.split()
        data.append([patterns, output])
    return data


if __name__ == '__main__':
    print(main())
