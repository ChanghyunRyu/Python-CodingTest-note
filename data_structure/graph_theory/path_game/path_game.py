import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data, number):
        self.data = data
        self.number = number
        self.left = None
        self.right = None


def add_node(root, data, number):
    if data[0] > root.data[0]:
        if root.right is None:
            root.right = Node(data, number)
        else:
            add_node(root.right, data, number)
    else:
        if root.left is None:
            root.left = Node(data, number)
        else:
            add_node(root.left, data, number)


def preorder(root, order):
    if root is not None:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)


def postorder(root, order):
    if root is not None:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.number)


def solution(node_info):
    node_info = [[*info, idx+1] for idx, info in enumerate(node_info)]
    node_info = sorted(node_info, key=lambda x: x[1], reverse=True)
    root = Node(node_info[0][:2], node_info[0][2])
    for info in node_info[1:]:
        data = info[:2]
        number = info[2]
        add_node(root, data, number)
    preorder_list = []
    preorder(root, preorder_list)
    postorder_list = []
    postorder(root, postorder_list)
    answer = [preorder_list, postorder_list]
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
