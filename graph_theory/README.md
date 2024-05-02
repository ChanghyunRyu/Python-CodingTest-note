## 그래프 이론(Graph Theory)

---

**그래프 이론(Graph Theory)** 은 수학에서 객체 간에 짝을 이루는 관계를 모델링하기 위해 사용되는 수학 구조인 그래프에 대한 이론을 말한다.

그래프는 정점(Vertex)과 정점을 연결하는 변(Edge)로 구성되어 있다. 정점을 컴퓨터 공학에서는 노드(node)라고 부르기도 한다.
변을 화살표로 나타내는 경우, 해당 방향으로만 이동할 수 있어 이러한 그래프를 **유향 그래프(Directed Graph)** 라고 한다. 
반대로 화살표가 없는 경우 양방향으로 이동할 수 있다는 뜻이며 이러한 그래프를 **무향 그래프(Undirected Graph)** 라고 한다.

이러한 그래프는 노드의 상태뿐 아니라 노드간의 연결 상태(상호작용)을 변을 사용하여 표현할 수 있다. 
예를 들어 정점을 각 도시, 변을 도로의 길이라고 했을 때 해당 그래프는 간단한 지도로 표현될 수 있다. 
이처럼 그래프는 복잡계를 구성하는 요소들의 상호작용을 표현하기 위한 수단으로 사용된다. 

---

#### 신장 트리(Spanning Tree)

그래프 내의 모든 정점을 포함하는 트리로 간선의 수가 가장 적은 최소 연결 부분 그래프이다.
n개의 정점을 가지는 그래프의 최소 간선의 수는 (n-1)개이고, (n-1)개의 간선으로 연결되어 있으면 이 그래프는 트리 형태가 되며 이를 스패닝 트리라고 한다. 

<image src="https://github.com/ChanghyunRyu/Python_CodingTest_note/assets/83490220/71ddc308-d342-4bce-8a0f-f6f20000ad50">

- 하나의 그래프에는 많은 신장 트리가 있을 수 있다.
- 모든 정점들이 연결되어 있어야 하고 사이클을 포함해서는 안 된다.
- n개의 정점을 (n-1)개의 간선으로 연결한다.

그래프에서 최소 비용으로 신장 트리를 만드는 알고리즘을 최소 신장 트리 알고리즘이라고 하며 크루스칼 알고리즘, 프림 알고리즘 등이 이에 해당한다.

- [**크루스칼 알고리즘(Kruskal Algorithm)**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/kruskal_algorithm)
- [**프림 알고리즘(Prim's Algorithm)**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/prims_algorithm)
