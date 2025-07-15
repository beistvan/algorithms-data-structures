import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

n = int(input())
tree = []
has_parent = [False] * n

for i in range(n):
    key, left, right = map(int, input().split())
    tree.append(Node(key, left, right))
    if left != -1:
        has_parent[left] = True
    if right != -1:
        has_parent[right] = True

if n == 0:
    print("CORRECT")
else:
    root = -1
    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    stack = []
    current = root
    prev = None
    correct = True

    while stack or current != -1:
        while current != -1:
            stack.append(current)
            current = tree[current].left
        current = stack.pop()
        key = tree[current].key
        if prev is not None and key <= prev:
            correct = False
            break
        prev = key
        current = tree[current].right
