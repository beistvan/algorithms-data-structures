def compute_height(n, parents):
    from collections import defaultdict, deque

    tree = defaultdict(list)
    root = -1

    for child, p in enumerate(parents):
        if p == -1:
            root = child
        else:
            tree[p].append(child)

    max_height = 0
    stack = [(root, 1)]

    while stack:
        node, depth = stack.pop()
        max_height = max(max_height, depth)
        for child in tree[node]:
            stack.append((child, depth + 1))

    return max_height

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    print(compute_height(n, parents))
