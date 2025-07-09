def process(commands):
    stack = []
    max_stack = []
    result = []

    for cmd in commands:
        if cmd.startswith("push"):
            _, val = cmd.split()
            val = int(val)
            stack.append(val)
            if not max_stack or val >= max_stack[-1]:
                max_stack.append(val)
            else:
                max_stack.append(max_stack[-1])

        elif cmd == "pop":
            if stack:
                stack.pop()
                max_stack.pop()

        elif cmd == "max":
            if max_stack:
                result.append(max_stack[-1])
            else:
                result.append(None)

    return result

if __name__ == "__main__":
    n = int(input())
    commands = [input().strip() for _ in range(n)]
    output = process(commands)
    for val in output:
        print(val)
