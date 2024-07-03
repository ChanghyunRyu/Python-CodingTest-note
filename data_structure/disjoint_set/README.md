## 서로소 집합(Disjoint Set)

---

**서로소 집합(Disjoint Set)이란**, 공통 원소가 없는 두 집합이다. 

서로소 집합 자료구조는 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조이다. 같거나 다른 집합으로 분리해주거나 혹은 최대 N개의 집합으로 분리하는 기능을 한다. 서로소 집합은 두가지 연산을 한다.

- Union(x, y): x가 속한 집합과 y가 속한 집합을 합친다.
- Find(x): x가 속한 집합의 루트 노드를 반환한다.

그래서 Union-Find 로 불리기도 한다. 연산 과정은 다음과 같다.

1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.  
    1-1. A와 B의 루트 노드 A'와 B'를 각각 찾는다.  
    1-2. A'를 B'의 부모노드로 설정한다.
2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다. 

[**Python을 통한 Union-Find 연산 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/data_structure/disjoint_set/union-find.py)

위의 방법대로 서로소 집합 자료구조를 구현하는 경우, 연산의 시간 복잡도가 O(VM) (V는 노드의 개수, M은 연산의 개수)가 되어 비효율적일 수 있다.
따라서 find 함수를 최적화라는 것이 필요하다.   

이러한 최적화는 경로 압축(Path Compression) 기법을 사용하여 find 함수를 변경해주면 간단하게 최적화가 가능하다.
~~~
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
~~~

### 서로소 집합을 활용한 사이클 판별

서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있는 특징이 있다. 과정은 다음과 같다.

1. 각 간선을 확인하여 두 노드의 루트 노드를 확인하다.  
    1.1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.  
    1.2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
2. 그래프에 포함된 모든 간선에 대하여 1번 과정을 반복한다.

[**Python을 통한 사이클 판별 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/data_structure/disjoint_set/cycle_check.py)

---

### Problem Solved

- [**섬 연결하기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set/connecting_islands)
- [**1717번 집합의 표현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set/1717_expression_of_set)
- [**1976번 여행 가자**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set/1976_lets_travel)
- [**4195번 친구 네트워크**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set/4195_friends_network)
- [**20040번 사이클 게임**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/data_structure/disjoint_set/20040_cycle_game)