## 호텔 방 배정

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/64063

"스노우타운"에서 호텔을 운영하고 있는 "스카피"는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 
호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 
처음에는 모든 방이 비어 있으며 "스카피"는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.

1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
2. 고객은 투숙하기 원하는 방 번호를 제출합니다.
3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.

예를 들어, 방이 총 10개이고, 
고객들이 원하는 방 번호가 순서대로 [1, 3, 4, 1, 3, 1] 일 경우 다음과 같이 방을 배정받게 됩니다.

| 원하는 방 번호 | 배정된 방 번호 |
|----------|----------|
| 1        | 1        |
| 3        | 3        |
| 4        | 4        |
| 1        | 2        |
| 3        | 5        |
| 1        | 6        |

전체 방 개수 k와 고객들이 원하는 방 번호가 순서대로 들어있는 배열 room_number가 매개변수로 주어질 때, 
각 고객에게 배정되는 방 번호를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- k는 1 이상 10^12 이하인 자연수입니다.
- room_number 배열의 크기는 1 이상 200,000 이하입니다.
- room_number 배열 각 원소들의 값은 1 이상 k 이하인 자연수입니다.
- room_number 배열은 모든 고객이 방을 배정받을 수 있는 경우만 입력으로 주어집니다.
  - 예를 들어, k = 5, room_number = [5, 5] 와 같은 경우는 방을 배정받지 못하는 고객이 발생하므로 이런 경우는 입력으로 주어지지 않습니다.

---
### Problem Solved Check
- [x] 1회 24/06/11
- [x] 2회 24/10/15
- [ ] 3회


아래는 완전한 풀이가 아닌 불완전한 풀이이다.  
간단하게 생각할 수 있는 풀이지만 해당 문제는 k는 10^12 으로 매우 큰 크기이고 room_number 배열 역시 200,000로 큰 숫자이다.  
해당 풀이의 시간 복잡도는 O(k*room_number)이므로 정확성 테스트는 모두 통과하지만 효율성 테스트에서는 문제가 발생하게 된다.
~~~
def solution(k, room_number):
    answer = []
    for r in room_number:
        assign_room(r, answer)
    return answer


def assign_room(number, a):
    if number in a:
        assign_room(number+1, a)
    else:
        a.append(number)
        
~~~

정답은 hotel_room_assign_2.py 처럼 풀이해야한다.  
1. 딕셔너리 자료형을 이용하여 방이 비어있는지를 검색하는 속도를 향상시키고
2. 딕셔너리 자료형에서 해당 방이 비어있지 않다면 비어있는 다음 방을 찾아 해당 숫자를 딕셔너리에 저장한다.

이렇게 되면 방이 비어있는 여부를 체크하는 속도와 비어있는 방을 확인하는 속도가 빨라져 해당 문제를 해결할 수 있다.

~~~
import sys
sys.setrecursionlimit(3000)


def solution(k, room_number):
    answer = []
    room = dict()
    for r in room_number:
        answer.append(assign_room(r, room))
    return answer


def assign_room(number, rooms):
    if number not in rooms:
        rooms[number] = number+1
        return number
    empty = assign_room(rooms[number], rooms)
    rooms[number] = empty+1
    return empty

~~~
~~~
import sys
sys.setrecursionlimit(100000)
record = {}


def solution(k, room_number):
    answer = []
    for number in room_number:
        answer.append(assign_room(number))
    return answer


def assign_room(room_number):
    if room_number not in record:
        record[room_number] = room_number+1
        assign_number = room_number
    else:
        assign_number = assign_room(record[room_number])
        record[room_number] = assign_number+1
    return assign_number
    
~~~

복습 시 틀린 점: 여러번 풀어 보았기에 바로 풀이는 알았지만 재귀 함수 이후, 딕셔너리에 방 번호를 배정하는 부분을 까먹어서 오답이 나왔다.

~~~
import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    answer = []
    hotel = {}
    for number in room_number:
        answer.append(assign_room(hotel, number))
    return answer


def assign_room(hotel, room_number):
    if room_number not in hotel:
        hotel[room_number] = room_number+1
        return room_number
    else:
        assign_number = assign_room(hotel, hotel[room_number])
        hotel[room_number] = assign_number
        return assign_number
        
~~~