def main():
    f = open("demo.txt", "r")
    f = open("input.txt", "r")
    data = parse(f)
    return middle_score(data)


def middle_score(data):
    all_scores = scores(data)
    return sorted(all_scores)[len(all_scores) // 2]


def scores(data):
    ans = []

    for line in data:
        stack = is_not_corrupted(line)
        if stack:
            ans.append(score(stack))

    return ans


def score(stack):
    score = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    ans = 0
    while stack:
        tail = stack.pop()
        ans *= 5
        ans += score[tail]
    return ans


def is_not_corrupted(line):
    match = {
        ']': '[',
        ')': '(',
        '}': '{',
        '>': '<'
    }
    stack = []
    for char in line:
        # if the char is a starting char
        if char not in match:
            stack.append(char)
            continue
        # otherwise it is one of the close characters
        # if the stack is empty, go to the next line
        if not stack:
            return None
        # if the character doesn't match
        if stack[-1] != match[char]:
            return None
        # remove from stack
        stack.pop()
    return stack


def parse(input):
    return [line.strip() for line in input]


if __name__ == '__main__':
    print(main())
