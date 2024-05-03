# 큐(Queue)

------

큐(Queue)는 기본적인 자료 구조의 한가지로, 먼저 집어넣은 데이터가 먼저 나오는 선입선출(FIFO, First In First Out)구조로 저장하는 형식을 말한다.  
데이터가 들어오는 위치는 가장 뒤에 있고, 나가는 위치는 제일 앞에 위치하여 먼저 들어오는 데이커가 먼저 나가게 된다.

[**Python을 이용한 Queue 구현**]()

### 우선순위 큐(Priority Queue)

- 먼저 들어오는 데이터가 아닌 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조
- 일반적으로 **힙(Heap)** 이라고 하는 완전이진트리 형태의 자료구조를 이용하여 구현된다.

### 힙(Heap)

- 완전이진트리 형태로 이루어져 있다.
- 부모노드와 서브트리간 대소 관계가 성립된다.(반정렬 상태)
- 이진탐색트리(BST)와 달리 중복된 값이 허용된다.

****
### Problem Solved

- [**강의실 배정**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/queue%26heap/classroom%20assignment)
- [**보석 도둑**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/queue%26heap/jewel%20thief)
- [**1715번 최소힙**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/queue%26heap/1927_min_heap)
- [**11236번 절댓값 힙**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/queue%26heap/11286_absolute_heap)