## 튜플

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/64065

셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. 
n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.

- (a1, a2, a3, ..., an)

튜플은 다음과 같은 성질을 가지고 있습니다.

1. 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
2. 원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
3. 튜플의 원소 개수는 유한합니다.

원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 
이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

- {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- s의 길이는 5 이상 1,000,000 이하입니다.
- s는 숫자와 '{', '}', ',' 로만 이루어져 있습니다.
- 숫자가 0으로 시작하는 경우는 없습니다.
- s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
- s가 표현하는 튜플의 원소는 1 이상 100,000 이하인 자연수입니다.
- return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어집니다.

---
### Problem Solved Check
- [x] 1회 24/05/21
- [x] 2회 24/07/23
- [x] 3회 24/10/15

보통 풀이를 할 때, 문자열을 하나씩 보면서 푸는 방법을 많이 사용했으나, split() 함수를 사용하여 쉽게 풀 수 없는지 확인해야 할 것.(3번째 풀이)
~~~
def solution(s):
    answer = []
    tmp = [0]*501
    tmp[0] = set([])
    in_set = False
    for i in range(1, len(s)-1):
        if s[i] == '{':
            start = i+1
            tmp_set = set()
            in_set = True
        elif in_set and s[i] == ',':
            tmp_set.add(int(s[start:i]))
            start = i+1
        elif s[i] == '}':
            in_set = False
            tmp_set.add(int(s[start:i]))
            tmp[len(tmp_set)] = tmp_set
    for i in range(1, len(tmp)):
        if tmp[i] == 0:
            break
        answer.append(list(tmp[i]-tmp[i-1])[0])
    return answer
   
~~~
~~~
def solution(s):
    answer = []
    sets = string_to_set(s[1:len(s)-1])
    sets.sort(key=len)
    before_set = set()
    for s in sets:
        new_int = s-before_set
        answer.append(list(new_int)[0])
        before_set = s
    return answer


def string_to_set(s):
    result = []
    is_set = False
    for i in range(len(s)):
        if s[i] == '{':
            temp = set()
            start = i+1
            is_set = True
        elif s[i] == '}':
            temp.add(int(s[start:i]))
            result.append(temp)
            is_set = False
        elif is_set and s[i] == ',':
            temp.add(int(s[start:i]))
            start = i+1
    return result
    
~~~
~~~
def solution(s):
    answer = {}
    data = s[2:-2].split('},{')

    data.sort(key=len)
    for d in data:
        nums = d.split(',')
        for num in nums:
            if num not in answer:
                answer[int(num)] = True
    return list(answer)
    
~~~
