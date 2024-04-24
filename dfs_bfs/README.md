# DFS / BFS

------

### DFS(Depth-First Search) 

DFS(깊이 우선 탐색)이란 루트 노드(혹은 다른 임의의 노드)에서 시작해 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법.  
미로를 탈출한다고 할 때, 한 방향으로 갈 수 있을 때까지 계속 진행한 후 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와 다른 방향으로 다시 탐색을 진행하는 방법.  

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
3. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
4. 2~3번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

모든 노드를 방문하고자 하는 경우에 이 방법을 주로 선택한다.

[**Python DFS 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24479_depth_first_search_1)

### BFS(Breadth-First Search)  

BFS(너비 우선 탐색)이란 루트 노드(혹은 다른 임의의 노드)에서 시작해 인접한 노드를 먼저 탐색하는 방법.  
시작점으로부터 가까운 노드를 먼저 방문한 후, 멀리 떨어져 있는 노드를 나중에 방문하는 순회 방법.  

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입한다.
3. 2번의 과정을 수행할 수 없을 때까지 반복한다.

두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택한다.
탐색 수행함에 있어 O(N) 시간이 소모되어 일반적인 경우, DFS보다 수행 시간이 좋은편에 속한다.

[**Python BFS 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24444_breadth_first_search_1)

------

### Problem Solved

- [**1012번 유기농 배추**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/1012_organic_cabbage)
- [**1260번 DFS와 BFS**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/dfs_bfs)  
- [**1697번 숨박꼭질**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/1697_hide_and_seek)
- [**2178번 미로탐색**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/2178_maze_search)
- [**2206번 벽 부수고 이동하기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/2206_crashing_wall)
- [**2606번 바이러스**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/2606_virus)
- [**2667번 단지번호붙이기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/2667_numbering)
- [**7562번 나이트의 이동**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/7562_knight's_movement)
- [**7569번 토마토**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/7569_tomato_3D)
- [**7576번 토마토**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/7576_tomato)
- [**16928번 뱀과 사다리**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/16928_snake_and_ladder)
- [**24444번 알고리즘 수업 - 너비 우선 탑색 1**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24444_breadth_first_search_1)
- [**24445번 알고리즘 수업 - 너비 우선 탐색 2**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24445_breadth_first_search_2)
- [**24479번 알고리즘 수업 - 깊이 우선 탐색 1**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24479_depth_first_search_1)
- [**24480번 알고리즘 수업 - 깊이 우선 탐색 2**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dfs_bfs/24480_depth_first_search_2)