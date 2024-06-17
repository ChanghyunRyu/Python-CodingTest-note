class Node:
    def __init__(self, item=0):
        self.key = item
        self.left, self.right = None, None


def insert_node(root, key):
    if root is None:
        root = Node(key)
        return root
    if key < root.key:
        root.left = insert_node(root.left, key)
    else:
        root.right = insert_node(root.right, key)
    return root


def tree_insert(data, root):
    for key in data:
        root = insert_node(root, key)


def in_order_rec(root, answer):
    if root is not None:
        in_order_rec(root.left, answer)
        answer.append(root.key)
        in_order_rec(root.right, answer)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
answer = []
r = Node()
tree_insert(array, r)
in_order_rec(r, answer)
print(answer[1:])
