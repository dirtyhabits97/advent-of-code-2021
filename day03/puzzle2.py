from collections import defaultdict

def main(nums, bin_len):
    # 1. calculate the count of every bit
    count = [0] * bin_len

    for num in nums:
        mask = 1 << (len(count) - 1)

        for idx in range(len(count)):
            count[idx] += 1 if mask & num else -1
            mask >>= 1

    # 2. check if should be 1 (true) or 0 (false)
    # based on the bit count
    oxy_bits = [x >= 0 for x in count]
    co2_bits = [x <= 0 for x in count]

    oxy, co2 = filter_by_col(nums, oxy_bits), filter_by_col(nums, co2_bits)

    return build(oxy, co2)


def filter_by_col(nums, bits_to_match):
    skip = defaultdict(lambda: False)
    mask = 1 << (len(bits_to_match) - 1)
    last_valid_num = float("inf")

    for bit in bits_to_match:

        for num in nums:
            # check if invalid
            if skip[num]:
                continue

            # check the mask
            if bit and mask & num:
                last_valid_num = num
            elif not bit and not mask & num:
                last_valid_num = num
            else:
                skip[num] = True
                continue  # invalid

        mask >>= 1

    ans = []
    for key in skip:
        if skip[key]:
            continue
        ans.append(skip[key])

    return ans if ans else [last_valid_num]


def filter(nums, count):

    # 1. oxygen
    oxygen = []
    for num in nums:

        skip = False
        mask = 1 << (len(count) - 1)
        for c in count:
            if c >= 0 and mask & num:
                skip = False
            elif c < 0 and not mask & num:
                skip = False
            else:
                skip = True
                break
            mask >>= 1

        if skip:
            continue

        print("adding to oxygen", num)
        oxygen.append(num)

    # 2. co2
    co2 = []
    for num in nums:

        skip = False
        mask = 1 << (len(count) - 1)

        for c in count:
            if c <= 0 and not mask & num:
                skip = False
            elif c > 1 and mask & num:
                skip = False
            else:
                skip = True
                break
            mask >>= 1

        if skip:
            continue

        print("adding to co2", num)
        co2.append(num)

    return (oxygen, co2)


def build(lhs, rhs):
    return sum(lhs) * sum(rhs)


if __name__ == '__main__':
    f = open("input.txt", "r")
    arr = []
    for line in f:
        binary = int(line, 2)
        arr.append(binary)
    print(main(arr, 12))
