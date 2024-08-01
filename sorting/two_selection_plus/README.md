## 두 개 뽑아서 더하기

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/68644

정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 
모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

---

~~~
from itertools import combinations


def solution(numbers):
    combination = combinations(numbers, 2)
    temp = set()
    for com in map(list, combination):
        num1 = com[0]
        num2 = com[1]
        temp.add(num1+num2)
    answer = list(temp)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))

~~~
~~~
import itertools


def solution(numbers):
    answer = set()
    for combination in itertools.combinations(numbers, 2):
        answer.add(combination[0]+combination[1])
    return sorted(list(answer))
    
~~~