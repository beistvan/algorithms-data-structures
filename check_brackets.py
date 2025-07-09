def check_brackets(text):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for i, char in enumerate(text):
        if char in pairs:
            stack.append((char, i + 1))
        elif char in pairs.values():
            if not stack:
                return i + 1
            top, pos = stack.pop()
            if pairs[top] != char:
                return i + 1

    if stack:
        return stack[0][1]

    return "Success"

if __name__ == "__main__":
    import sys
    input_text = sys.stdin.read().strip()
    print(check_brackets(input_text))
