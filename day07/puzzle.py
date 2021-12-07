def main():
    f = open("input.txt", "r")
    input = list(map(int, f.readline().split(",")))
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    return align(input)


def align(input):
    """
    0       1       1       2       2       2       4       7       14      16
    """
    input.sort()
    mid = input[len(input)//2]
    ans = 0

    for num in input:
        ans += abs(num - mid)
    return ans


if __name__ == '__main__':
    print(main())
