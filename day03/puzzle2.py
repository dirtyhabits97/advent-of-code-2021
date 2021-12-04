from collections import defaultdict


def life_support_rating(nums, number_of_bits):
    oxy, co2 = [], []

    while len(oxy) != 1:
        oxy = bit_criteria(nums, number_of_bits, True)

    while len(co2) != 1:
        co2 = bit_criteria(nums, number_of_bits, False)

    return oxy[0] * co2[0]


def bit_criteria(nums, cols, find_most_common):
    skip = defaultdict(lambda: False)
    mask = 1 << (cols - 1)
    last_valid_num = float("inf")

    for _ in range(cols):

        # find the most or least common bit
        number_of_one_bits = 0
        for num in nums:
            if skip[num]:
                continue
            number_of_one_bits += 1 if num & mask else -1

        # check what the target bit is for this position
        # if default to one = True, we are calculating oxygen
        if find_most_common:
            target = 1 if number_of_one_bits >= 0 else 0
        # find the least common
        else:
            target = 0 if number_of_one_bits >= 0 else 1

        for num in nums:
            if skip[num]:
                continue
            if target and (num & mask):
                last_valid_num = num
            elif not target and not (num & mask):
                last_valid_num = num
            else:
                skip[num] = True

        mask >>= 1

    ans = []
    for num in skip:
        if skip[num]:
            continue
        ans.append(num)

    return ans if ans else [last_valid_num]


if __name__ == '__main__':
    f = open("input.txt", "r")
    arr = []
    for line in f:
        binary = int(line, 2)
        arr.append(binary)
    print(life_support_rating(arr, 12))
