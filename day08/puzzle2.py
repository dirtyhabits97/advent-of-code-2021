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
    For this first puzzle, to find occurrences of 1, 4, 7 and 8 we count
    the str length.
    1 -> 2 chars to represent
    4 -> 4 chars to represent
    7 -> 3 chars to represent
    8 -> 7 chars to represent
    """
    ans = 0
    for signals, outputs in data:
        nums = find_numbers(signals)
        ans += build_number(nums, outputs)

        continue

        print("==============================")
        zero = set()
        one = set()
        two = set()
        three = set()
        four = set()
        five = set()
        six = set()
        seven = set()
        eight = set()
        nine = set()

        len_5_numbers = []
        len_6_numbers = []

        for signal in signals:
            # 1
            if len(signal) == 2:
                one = set(signal)
                print("1: ", one)
            # 4
            elif len(signal) == 4:
                four = set(signal)
                print("4: ", four)
            # 7
            elif len(signal) == 3:
                seven = set(signal)
                print("7: ", seven)
            # 8
            elif len(signal) == 7:
                eight = set(signal)
                print("8: ", eight)

            # 2, 3 or 5
            elif len(signal) == 5:
                len_5_numbers.append(set(signal))
                print("2, 3 or 5: ", len_5_numbers)
            # 0, 6 or 9
            elif len(signal) == 6:
                len_6_numbers.append(set(signal))
                print("0, 6 or 9: ", len_6_numbers)
        print("==============================")

        top = seven.symmetric_difference(one)
        four_minus_one = four.symmetric_difference(one)

        print("top: ", top)
        print("4 has ", four_minus_one, "which 1 doesn't have")

        # find 5
        top_right = set()
        bottom_right = set()
        for candidate in len_5_numbers:
            if four_minus_one.issubset(candidate):
                five = candidate
                print("5: ", five)

                top_right = one.difference(five)
                print("top right:", top_right)

                bottom_right = one.difference(top_right)
                print("bottom right: ", bottom_right)
        len_5_numbers.remove(five)

        # find 6
        for candidate in len_6_numbers:
            if candidate.issuperset(bottom_right) and not candidate.issuperset(top_right):
                six = candidate
                print("6: ", six)
        len_6_numbers.remove(six)

        # find 2
        for candidate in len_5_numbers:
            print(top_right, candidate)
            if candidate.issuperset(bottom_right):
                three = candidate
            else:
                two = candidate

        print("2: ", two)
        print("3: ", three)

        print("Now we need to find 0 vs 9")
        eight_minus_three = eight.difference(three)
        print("if we subtract 8 -3, we get the top and bottom left:", eight_minus_three)

        for candidate in len_6_numbers:
            if candidate.issuperset(eight_minus_three):
                zero = candidate
            else:
                nine = candidate

        print("0: ", zero)
        print("9: ", nine)

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]
        for idx in range(len(nums)):
            print(idx, nums[idx])

        num_to_add = 0
        for output in outputs:
            o = set(output)
            for idx in range(len(nums)):
                num = nums[idx]
                if num == o:
                    num_to_add *= 10
                    num_to_add += idx
        ans += num_to_add
        print(num_to_add)

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
        if candidate.issuperset(bottom_right) and not candidate.issuperset(top_right):
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
    # we can get bottom left by subtracting '3' from '8', this will give us top left too,
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
        # match with a deciphered number
        ans *= 10
        # TODO: delete this print
        print(nums)
        ans += nums.index(set(output))
    return ans


"""
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
8       5     2     3     7   9      6      4    0      1    5     3     5     3

top = d (7 has d, 1 doesn't)

4 has e and f which 1 doesn't have. Number 5 should have len=5 and e and f

5 has b but no a, meaning:
top right = a
bottom right = b

6 is len=6 and b but no a

2 is len=5 and a but not b, 3 is len=5 and a and b

Now we need to find 0 vs 9

if we subtract 8 - 3, we get the top and bottom left:
e and g (don't know the order)

0 will have both e and g, 9 will only have 1
"""


if __name__ == '__main__':
    print(main())
