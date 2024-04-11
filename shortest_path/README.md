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

[**Python 다익스트라 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/dijkstra_algorithm)

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

- ### 벨만-포드 알고리즘(Bellman-Ford Algorithm)

가중 그래프에서 한 지점으로부터 다른 지점까지의 최단거리를 구하는 알고리즘이다.  
단, 위의 두 알고리즘과 달리 **간선의 가중치가 음수일 때도 최단 거리를 구할 수 있다**는 장점이 있다.  

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 모든 간선 E를 하나씩 확인한다.
4. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3부터의 과정을 각 노드에 대하여 (V-1)번 반복한다.
6. 음수 간선 순환이 발생하는지 체크하고 싶다면 위의 과정을 한 번더 수행하여 최단거리 테이블이 갱신되는지 확인한다.

[**Python 벨만-포드 알고리즘 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/11657_timemachine)

------

### Problem solved

- [**1238번 파티**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/1238_party)
- [**1504번 특정한 최단 경로**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/1504_specific_shortest_path)
- [**1753번 최단 경로**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/1753_shortest_path)
- [**1956번 운동**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/1956_work_out)
- [**9370번 미확인 도착지**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/9370_unconfirmed_destination)
- [**11404번 플로이드**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/11404_floyd)
- [**11657번 타임머신**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/11657_timemachine)
- [**13549번 숨박꼭질 3**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/shortest_path/13549_hide_and_seek_3)