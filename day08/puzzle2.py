def main():
    f = open("input.txt", "r")
    data = parse(f)

    return sum_outputs(data)


def parse(input):
    data = []
    for line in input:
        patterns, output = line.split("|")
        patterns, output = patterns.split(), output.split()
        data.append([patterns, output])
    return data


def sum_outputs(data):
    """
    Expected input:
    [
        # [signals], [output]
        ['be', 'cfbegad', ...], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'],
        ...
    ]
    """
    ans = 0
    for signals, outputs in data:
        nums = find_numbers(signals)
        ans += build_number(nums, outputs)
    return ans


def find_numbers(signals):
    nums = [set() for _ in range(10)]
    len_5_numbers, len_6_numbers = group_numbers(nums, signals)

    # find 5
    # if we subtract '1' from '4', we get top left and midddle
    # '5' has top left and middle, while '2' and '3' don't
    four_minus_one = nums[4].difference(nums[1])
    # these will help us find 6
    top_right, bottom_right = set(), set()
    for candidate in len_5_numbers:
        if candidate.issuperset(four_minus_one):
            nums[5] = candidate

            top_right = nums[1].difference(nums[5])
            bottom_right = nums[1].difference(top_right)
            break
    len_5_numbers.remove(nums[5])

    # find 6
    # '6' has bottom_right but not top_right
    # '0' and '9' have both top and bottom right
    for candidate in len_6_numbers:
        if candidate.issuperset(bottom_right) and \
                not candidate.issuperset(top_right):

            nums[6] = candidate
            break
    len_6_numbers.remove(nums[6])

    # find 2 and 3
    # '2' has top right but not bottom right
    # '3' has both
    for candidate in len_5_numbers:
        if candidate.issuperset(bottom_right):
            nums[3] = candidate
        else:
            nums[2] = candidate

    # find 0 and 9
    # '9' doesn't have bottom left
    # '0' does have bottom left
    # we can get bottom left by subtracting '3' from '8' (top left included),
    # '0' will be a super set of this result, 9 won't
    eight_minus_three = nums[8].difference(nums[3])
    for candidate in len_6_numbers:
        if candidate.issuperset(eight_minus_three):
            nums[0] = candidate
        else:
            nums[9] = candidate
    return nums


def group_numbers(nums, signals):
    # len 5: 2, 3 or 5
    # len 6: 0, 6 or 9
    len_5_numbers, len_6_numbers = [], []
    for signal in signals:
        if len(signal) == 2:
            nums[1] = set(signal)
        elif len(signal) == 4:
            nums[4] = set(signal)
        elif len(signal) == 3:
            nums[7] = set(signal)
        elif len(signal) == 7:
            nums[8] = set(signal)
        elif len(signal) == 5:
            len_5_numbers.append(set(signal))
        elif len(signal) == 6:
            len_6_numbers.append(set(signal))

    return (len_5_numbers, len_6_numbers)


def build_number(nums, outputs):
    ans = 0
    for output in outputs:
        ans *= 10
        # match with a deciphered number
        ans += nums.index(set(output))
    print(outputs, "  \t\t=> ", ans)
    return ans


if __name__ == '__main__':
    print(main())
