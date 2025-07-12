def find_occurrences(pattern, text):
    result = []
    p_len = len(pattern)
    t_len = len(text)

    for i in range(t_len - p_len + 1):
        if text[i:i + p_len] == pattern:
            result.append(i)
    return result

def main():
    pattern = input().strip()
    text = input().strip()
    positions = find_occurrences(pattern, text)
    print(" ".join(map(str, positions)))

if __name__ == "__main__":
    main()
