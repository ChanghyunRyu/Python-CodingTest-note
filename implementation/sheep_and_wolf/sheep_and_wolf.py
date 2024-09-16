def solution(info, edges):
    nodes = {}
    for root, child in edges:
        if root not in nodes:
            nodes[root] = Node(root)
        if child not in nodes:
            nodes[child] = Node(child)
        nodes[root].insert_node(nodes[child])

    def dfs(now, cage, possible_node, result):
        if now is None:
            return
        cage[info[now.data]] += 1
        if cage[0] <= cage[1]:
            return
        result[0] = max(result[0], cage[0])
        for new_node in possible_node:
            temp = set(possible_node)
            if new_node.left is not None:
                temp.add(new_node.left)
            if new_node.right is not None:
                temp.add(new_node.right)
            temp.remove(new_node)
            dfs(new_node, list(cage), temp, result)

    answer = [0]
    start_node = nodes[0]
    start_set = set()
    if start_node.left is not None:
        start_set.add(start_node.left)
    if start_node.right is not None:
        start_set.add(start_node.right)
    dfs(start_node, [0, 0], start_set, answer)
    return answer[0]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, new_node):
        if self.left is None:
            self.left = new_node
        else:
            if self.left.data < new_node.data:
                self.right = new_node
            else:
                self.right = self.left
                self.left = new_node


info_exam = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edge_exam = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
# result = 5
print(solution(info_exam, edge_exam))
