def main(nums):
    count = 0
    start = 0
    for end in range(3, len(nums)):
        # 1. check if the new number is greater than the
        # one we will remove
        if nums[end] > nums[start]:
            count += 1

        # 2. remove start from the window
        start += 1

    return count


if __name__ == "__main__":
    f = open("input.txt", "r")
    arr = []
    for line in f:
        arr.append(int(line))
    print(main(arr))
