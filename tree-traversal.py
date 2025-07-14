class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def in_order(index, tree, result):
    if index == -1:
        return
    in_order(tree[index].left, tree, result)
    result.append(tree[index].value)
    in_order(tree[index].right, tree, result)

def pre_order(index, tree, result):
    if index == -1:
        return
    result.append(tree[index].value)
    pre_order(tree[index].left, tree, result)
    pre_order(tree[index].right, tree, result)

def post_order(index, tree, result):
    if index == -1:
        return
    post_order(tree[index].left, tree, result)
    post_order(tree[index].right, tree, result)
    result.append(tree[index].value)

n = int(input())
tree = []
has_parent = [False] * n

for i in range(n):
    value, left, right = map(int, input().split())
    tree.append(Node(value, left, right))
    if left != -1:
        has_parent[left] = True
    if right != -1:
        has_parent[right] = True

root = has_parent.index(False)

in_result = []
pre_result = []
post_result = []

in_order(root, tree, in_result)
pre_order(root, tree, pre_result)
post_order(root, tree, post_result)

print(" ".join(map(str, in_result)))
print(" ".join(map(str, pre_result)))
print(" ".join(map(str, post_result)))
