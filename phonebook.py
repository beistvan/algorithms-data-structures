def phone_book(commands):
    book = {}
    result = []

    for command in commands:
        parts = command.split()
        operation = parts[0]
        number = int(parts[1])

        if operation == 'add':
            name = parts[2]
            book[number] = name
        elif operation == 'del':
            if number in book:
                del book[number]
        elif operation == 'find':
            result.append(book.get(number, "not found"))

    return result

n = int(input())
commands = [input().strip() for _ in range(n)]
results = phone_book(commands)
for res in results:
    print(res)
