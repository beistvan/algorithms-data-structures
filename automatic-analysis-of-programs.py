import sys

sys.setrecursionlimit(10**6)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root != y_root:
        parent[y_root] = x_root

def main():
    n, m_e, m_d = map(int, sys.stdin.readline().split())
    parent = list(range(n + 1))

    equalities = []
    inequalities = []

    for _ in range(m_e):
        a, b = map(int, sys.stdin.readline().split())
        equalities.append((a, b))

    for _ in range(m_d):
        a, b = map(int, sys.stdin.readline().split())
        inequalities.append((a, b))

    for a, b in equalities:
        union(a, b, parent)

    for a, b in inequalities:
        if find(a, parent) == find(b, parent):
            print(0)
            return

    print(1)

if __name__ == "__main__":
    main()
