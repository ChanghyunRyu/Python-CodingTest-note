# Sorting

------------
**정렬(Sorting)** 이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.

- **선택 정렬(Selection Sort):** 데이터를 오름차순으로 정렬한다고 할 때, 가장 작은 데이터를 찾아 선택해 맨 앞에 있는 데이터와 바꾸고 
    그다음 작은 데이터를 찾아 바꾸는 과정을 반복하여 정렬하는 방법.
  - 시간 복잡도: O(N^2)

[**Python을 이용한 선택 정렬 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/sorting/sort/selection_sort.py)

- **삽입 정렬(Insertion Sort):** 데이터 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여,
    자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 방법
  - 시간 복잡도: O(N^2)
  - 현재 리스트의 데이터가 거의 정렬되어 있는 경우, 매우 빠르게 동작.


[**Python을 이용한 삽입 정렬 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/sorting/sort/count_sort.py)

- **퀵 정렬(Quick Sort):** 분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법. 다음과 같은 방법으로 동작한다.  
  1. 리스트 안에 있는 한 요소를 선택한다. 이렇게 선택한 원소를 피벗(pivot)이라고 칭한다.
  2. 피벗의 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 큰 요소들은 모두 피벗의 오른쪽으로 옮긴다.
  3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
  4. 더 이상 분할이 불가능할 때까지 반복한다.
  - 시간 복잡도: 평균 O(NlogN), 최악의 경우 O(N^2)

[**Python을 이용한 퀵 정렬 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/sorting/sort/quick_sort_2.py)

- **계수 정렬(Counting Sort):** 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 경우만 사용이 가능하지만 
매우 빠르게 실행된다. 최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬을 수행한다. 
간단히 말하면 데이터 배열에서 각 원소가 나온 갯수를 세어 새로운 배열에 저장하는 것이다.
  - 시간 복잡도: O(N+K), K는 배열의 최댓값


[**Python을 이용한 계수 정렬 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/sorting/sort/count_sort.py)

- **위상 정렬(Topology Sort):** 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다. 유향 그래프의 노드들을 엣지의 방향을 거스르지 않도록 나열하는 것이다. 
위상 정렬을 하기 위해서는 그래프가 방향이 있으며 순환하지 않는 그래프여야 한다. 위상 정렬을 하는 Kahn 알고리즘은 다음과 같다.
  1. 진입차수가 0인 노드를 큐에 넣는다.
  2. 큐가 빌 때까지 다음 과정을 반복한다.
     1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
     2. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.

[**Python을 이용한 위상 정렬 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/blob/main/sorting/sort/topology_sort.py)

### Problem Solved

- [**단어 정렬**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/1181_word_sorting)
- [**두 개 뽑아서 더하기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/two_selection_plus)
- [**H-Index**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/h_index)
- [**문자열 내 마음대로 정렬하기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/string_as_i_want)
- [**가장 큰 수**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/biggest_num)
- [**1191번 단어 정렬**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/1181_word_sorting)
- [**1427번 소트인사이드**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/sorting/1427_sort_in_side)

