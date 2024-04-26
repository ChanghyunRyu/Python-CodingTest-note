## 크루스칼 알고리즘(Kruskal Algorithm)

---

**크루스칼 알고리즘(Kruskal Algorithm)이란,** 그래프 내의 모든 정점들을 가장 적은 비용으로 연결하기 위해 사용되는 최소 신장 트리 알고리즘이다.

**신장 트리** 란, 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.  
**최소 신장 트리 알고리즘** 란, 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘이다.  

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.  
    2.1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.  
    2.2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번 과정을 반복한다.

[**Python을 이용한 크루스칼 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/greedy_algorithm/kruskal_algorithm/kruskal_algorithm.py)

크루스칼 알고리즘 구현을 알아보기 이전에 서로소 집합 자료구조와 이를 이용한 사이클 판별법을 알아두는 것이 좋다.  

[**서로소 집합 자료구조**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set)


