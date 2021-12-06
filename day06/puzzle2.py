def calculate_population(nums, days):
    # Group the fishes by buckets,
    # instead of iterating every fish, iterate the array of days
    grouped = [0 for _ in range(9)]
    for num in nums:
        grouped[num] += 1

    for d in range(days):

        new = [0 for _ in range(9)]
        for idx in range(len(grouped)):

            if not idx:
                new[6] = grouped[idx]
                new[8] = grouped[idx]
            else:
                new[idx - 1] += grouped[idx]

        grouped = new
        print("grouped after day: ", d, grouped)

    return sum(grouped)


def main():
    f = open("input.txt", "r")
    input = list(map(int, f.readlines()[0].split(",")))
    # input = [3, 4, 3, 1, 2]
    print(calculate_population(input, 256))


if __name__ == '__main__':
    main()
