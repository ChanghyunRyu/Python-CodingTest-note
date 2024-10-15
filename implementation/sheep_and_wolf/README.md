## 양과 늑대

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/92343

2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다. 
이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다. 
각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다. 
이때, 늑대는 양을 잡아먹을 기회를 노리고 있으며, 당신이 모은 양의 수보다 
늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다. 
당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 
최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.

각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info, 
2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때, 
문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 
최대 몇 마리인지 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- 2 ≤ info의 길이 ≤ 17
  - info의 원소는 0 또는 1 입니다.
  - info[i]는 i번 노드에 있는 양 또는 늑대를 나타냅니다.
  - 0은 양, 1은 늑대를 의미합니다.
  - info[0]의 값은 항상 0입니다. 즉, 0번 노드(루트 노드)에는 항상 양이 있습니다.
- edges의 세로(행) 길이 = info의 길이 - 1
  - edges의 가로(열) 길이 = 2
  - edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태로, 서로 연결된 두 노드를 나타냅니다.
  - 동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
  - 항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.
  - 0번 노드는 항상 루트 노드입니다

---
### Problem Solved Check
- [X] 1회 24/09/16
- [ ] 2회
- [ ] 3회

다음 방문할 노드의 집합을 만드는 부분이 가장 중요한 문제, 
대충 어떻게 풀지는 생각했지만 저 부분을 구현 못해서 실패. 
~~~
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
                
~~~