def main(nums):
    # 1. calculate the count of every bit
    count = [0] * 12

    for num in nums:
        mask = 1 << (len(count) - 1)

        for idx in range(len(count)):
            count[idx] += 1 if mask & num else -1
            mask >>= 1

    # 2. calculate the power consumption
    return build(count)


def build(arr):
    """
    Receives a count array: [1,2,-3,-4]. If the number is
    above 0, then there should be a 1 in that position, if is
    below 0, then there should be a 0.
    """
    gamma, epsilon = 0, 0

    for count in arr:
        gamma <<= 1
        epsilon <<= 1

        if count > 0:
            gamma |= 1
        else:
            epsilon |= 1

    return gamma * epsilon


if __name__ == '__main__':
    f = open("input.txt", "r")
    arr = []
    for line in f:
        binary = int(line, 2)
        arr.append(binary)
    print(main(arr))
