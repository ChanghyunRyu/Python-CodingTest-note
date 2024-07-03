import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data, number):
        self.data = data
        self.number = number
        self.left = None
        self.right = None


def add_Node(root, new_node):
    if new_node.data[0] < root.data[0]:
        if root.left is None:
            root.left = new_node
        else:
            add_Node(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            add_Node(root.right, new_node)


def solution(node_info):
    node_info = [[*data, i+1] for i, data in enumerate(node_info)]
    node_info = sorted(node_info, key=lambda x: x[1], reverse=True)

    root = Node(node_info[0][:2], node_info[0][2])
    for i in range(1, len(node_info)):
        add_Node(root, Node(node_info[i][:2], node_info[i][2]))

    preorder_list = []
    preorder(root, preorder_list)

    postorder_list = []
    postorder(root, postorder_list)
    return [preorder_list, postorder_list]


def preorder(root: Node, result: list):
    if root is not None:
        result.append(root.number)
        preorder(root.left, result)
        preorder(root.right, result)


def postorder(root: Node, result: list):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.number)


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
