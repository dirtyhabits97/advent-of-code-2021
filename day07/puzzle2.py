def main():
    f = open("input.txt", "r")
    input = list(map(int, f.readline().split(",")))
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    return align(input)


def align(input):
    total, count = sum(input), len(input)
    target = sum(input) // len(input)

    print(total, count, target)

    return sum([calculate_cost(target, num) for num in input])


def calculate_cost(target, num):
    diff = abs(target - num)
    cost = sum([x for x in range(diff + 1)])
    print("cost from: ", num, "to: ", target, "is: ", cost)
    return cost


if __name__ == '__main__':
    print(main())
