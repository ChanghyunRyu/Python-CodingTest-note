# 최단 경로 알고리즘(Shortest-paht Algorithm)

------

최단 경로 알고리즘: '길찾기' 라고도 불리는 알고리즘으로 말 그대로 가장 짧은 경로를 찾는 알고리즘.

- ### 다익스트라 최단 경로 알고리즘(Dijkstra Algorithm)

다익스트라 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 최단 경로를 구해주는 알고리즘이다.

1. 모든 노드를 미방문 상태로 표시한다.
2. 모든 노드에 시험적 거리 값을 부여한다. (초기점=현재 위치를 0, 다른 모든 노드를 무한대로 설정)
3. 현재 노드에서 미방문 인접 노드를 찾아 시험적 거리를 현재 노드에서 계산, 새로 계산한 시험적 거리를 현재 부여된 값과 
   계산한 시험적 거리를 비교해서 더 작은 값을 넣는다.
   
4. 만약 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드를 방문 처리한다.
5. 두 꼭짓점 사이의 경로를 찾는 경우: 도착점이 방문한 상태로 표시되면 멈추고 알고리즘 종료
6. 완전 순회 경로를 찾는 경우: 미방문 노드들의 시험적 거리 중 최솟값이 무한대이면 이는 출발점과 미방문 집합 사이에 
   연결이 없는 경우이므로 알고리즘 종료
   
7. 아닌 경우, 시험적 거리가 가장 작은 다음 미방문 노드를 새로운 "현재 위치"로 선택하고 3으로 돌아간다.

[**Python 다익스트라 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/Dijkstra_algorithm)

- ### 플로이드 워셜 알고리즘(Floyd-Warshall Algorithm)

가중 그래프에서 모든 지점에서부터 다른 모든 지점까지의 최단 경로들을 찾는 알고리즘이다.  
1. 그래츠에 총 N개의 노드가 있다고 가정한다. 이 중 하나의 노드 K를 선택한다.
2. 선택한 노드는 K, K를 제외한 (N-1)개의 노드 중 서로 다른 두 노드 A, B를 선택한다.
3. A, B로 가는 거리와 K를 경유하여 A에서 B를 가는 거리를 비교하여 최단거리를 갱신한다.  
3-2. D(AB) = min(D(AB), D(AK)+D(KB)) 
4. 이를 모든 (n-1)개의 노드쌍에 대하여 실행한다.
5. 위의 과정을 모든 노드에 대하여 실행한다.

위를 실행하다 보면 해당 알고리즘이 다이나믹 프로그래밍의 성격을 가지고 있음을 알 수 있다.  
shortestPath(i, j, k) = min(shortestPath(i, j, k-1), shortestPath(i, k, k-1)+shortestPath(k, j, k-1))

[**Python 플로이드 워셜 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/floyd_warshall_algorithm)

------

### Problem solved

- [**1238번 파티**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/1238_party)
