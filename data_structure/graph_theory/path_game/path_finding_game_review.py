import sys
sys.setrecursionlimit(10**6)


class node:
    def __init__(self, data, number):
        self.data = data
        self.number = number
        self.left = None
        self.right = None


def add_node(root, new_node):
    if root.data[0] > new_node.data[0]:
        if root.left is None:
            root.left = new_node
        else:
            add_node(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            add_node(root.right, new_node)


def solution(nodeinfo):
    nodeinfo = [(i+1, info) for i, info in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1][1], reverse=True)
    root = node(data=nodeinfo[0][1], number=nodeinfo[0][0])
    for i in range(1, len(nodeinfo)):
        number, info = nodeinfo[i]
        new_node = node(number=number, data=info)
        add_node(root, new_node)
    preorder = []
    postorder = []
    get_preorder(root, preorder)
    get_postorder(root, postorder)
    return [preorder, postorder]


def get_preorder(root, result):
    if root is None:
        return
    result.append(root.number)
    get_preorder(root.left, result)
    get_preorder(root.right, result)


def get_postorder(root, result):
    if root is None:
        return
    get_postorder(root.left, result)
    get_postorder(root.right, result)
    result.append(root.number)


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
