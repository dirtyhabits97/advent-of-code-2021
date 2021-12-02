def main(nums):
    prev = float("inf")
    count = 0
    for num in nums:
        if num > prev:
            count += 1
        prev = num

    return count


if __name__ == "__main__":
    f = open("input.txt", "r")
    arr = []
    for line in f:
        arr.append(int(line))
    print(main(arr))
