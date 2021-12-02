def main(logs):
    position, depth, aim = 0, 0, 0

    for log, value in logs:
        if log == "forward":
            position += value
            depth += aim * value
        elif log == "down":
            aim += value
        elif log == "up":
            aim -= value

    return position * depth


if __name__ == '__main__':
    f = open("input.txt", "r")
    arr = []
    for line in f:
        split = line.split(" ")
        split[1] = int(split[1])
        arr.append(split)
    print(main(arr))
