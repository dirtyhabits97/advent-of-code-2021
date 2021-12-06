# This looks like a BFS problem where every parent is passed to the next level

def bfs(nums, days):
    for _ in range(days):
        for idx in range(len(nums)):

            if not nums[idx]:
                nums.append(8)
                nums[idx] = 6
            else:
                nums[idx] -= 1

    return len(nums)


def main():
    f = open("input.txt", "r")
    input = list(map(int, f.readlines()[0].split(",")))
    print(bfs(input, 256))


if __name__ == '__main__':
    main()
