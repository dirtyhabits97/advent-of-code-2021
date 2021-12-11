def main():
    f = open("demo.txt", "r")
    f = open("input.txt", "r")
    data = parse(f)
    return score(data)


def score(data):
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    ans = 0
    counter = count(data)
    print(counter)
    for char in counter:
        ans += (score[char] * counter[char])
    return ans


def count(data):
    match = {
        ']': '[',
        ')': '(',
        '}': '{',
        '>': '<'
    }
    count = {
        ']': 0,
        ')': 0,
        '}': 0,
        '>': 0
    }
    for line in data:
        stack = []
        for char in line:
            # if the char is a starting char
            if char not in match:
                stack.append(char)
                continue
            # otherwise it is one of the close characters
            # if the stack is empty, go to the next line
            if not stack:
                count[char] += 1
                print("expected ", match[char], " but the stack was empty")
                break
            # if the character doesn't match
            if stack[-1] != match[char]:
                count[char] += 1
                print("expected ", stack[-1], " but found ", char, " instead.")
                break
            # remove from stack
            stack.pop()
    return count


def parse(input):
    return [line.strip() for line in input]


if __name__ == '__main__':
    print(main())
