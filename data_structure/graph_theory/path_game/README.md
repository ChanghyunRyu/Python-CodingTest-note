## 길찾기 게임

---

길찾기 게임은 두 팀으로 나누어, 각 팀이 같은 곳을 다른 순서로 방문하도록 
해서 먼저 순회를 마친 팀이 승리하는 것이다.

방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후, 
순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

- 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
- 모든 노드는 서로 다른 x값을 가진다.
- 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
- 자식 노드의 y 값은 항상 부모 노드보다 작다.
- 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
- 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.

이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

### 제한 사항

- nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
  - nodeinfo의 길이는 1 이상 10,000 이하이다.
  - nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
  - 모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
  - 트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
  - 모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.

---
### Problem Solved Check
- [X] 1회 24/07/03 
- [ ] 2회
- [ ] 3회

이진 트리로 구성하여 전위, 후위탐색하는 것은 알았으나 트리로 만드는 부분을 본인이 직접 해결하지 못 했다.  
내일 다시 풀이를 해보는 것이 좋을 것으로 보인다.
~~~
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
    
~~~