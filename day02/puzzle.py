def main(logs):
    position, depth = 0, 0

    for log, value in logs:
        if log == "forward":
            position += value
        elif log == "down":
            depth += value
        elif log == "up":
            depth -= value

    return position * depth


if __name__ == '__main__':
    f = open("input.txt", "r")
    arr = []
    for line in f:
        split = line.split(" ")
        split[1] = int(split[1])
        arr.append(split)
    print(main(arr))
