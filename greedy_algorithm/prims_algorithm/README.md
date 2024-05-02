## 프림 알고리즘(Prim's Algorithm)

---

**프림 알고리즘(Prim's Algorithm)이란,** 그래프 내의 모든 정점들을 가장 적은 비용으로 연결하기 위해 사용되는 최소 신장 트리 알고리즘이다.

**신장 트리** 란, 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.  
**최소 신장 트리 알고리즘** 란, 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘이다.  

1. 임의의 정점을 선택하여 비어있는 트리 T에 포함시킨다.
2. T에 있는 노드와 T에 없는 노드 사이의 간선 중 가중치가 최소인 간선을 찾는다.
3. 찾은 간선이 연결하는 두 노드 중, T에 없던 노드를 T에 포함 시킨다.
4. 모든 노드가 T에 포함될 때까지 2, 3번을 반복한다.

프림 알고리즘의 시간복잡도는 O(V^2)로, 다익스트라 알고리즘처럼 우선순위 큐를 사용할 경우, O(ElogV)가 된다. (V = 정점의 개수, E= 간선의 개수)

[**Python을 이용한 프림 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/greedy_algorithm/prims_algorithm/prims_algorithm.py)

### 프림 알고리즘 vs 크루스칼 알고리즘

프림 알고리즘의 시간 복잡도는 O(ElogV)  
크루스칼 알고리즘의 시간 복잡도는 O(ElogE)  
따라서,그래프 내의 간선이 많은 경우는 프림 알고리즘이 간선이 적은 경우는 크루스칼 알고리즘이 유리하다.

---

### Problem Solved

- [**17472번 다리 만들기 2**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/kruskal_algorithm/17472_create_bridge_2)