## 체육 대회

---

[출처] https://school.programmers.co.kr/learn/courses/15008/lessons/121684

당신이 다니는 학교는 매년 체육대회를 합니다. 체육대회는 여러 종목에 대해 각 반의 해당 종목 대표가 1명씩 나와 대결을 하며, 
한 학생은 최대 한개의 종목 대표만 할 수 있습니다. 당신의 반에서도 한 종목당 1명의 대표를 뽑으려고 합니다. 학생들마다 각 종목에 대한 능력이 다르지만 이 능력은 수치화되어 있어 미리 알 수 있습니다. 당신의 반의 전략은 각 종목 대표의 해당 종목에 대한 능력치의 합을 최대화하는 것입니다.

당신의 반 학생들의 각 종목에 대한 능력치를 나타내는 2차원 정수 배열 ability가 주어졌을 때, 
선발된 대표들의 해당 종목에 대한 능력치 합의 최대값을 return 하는 solution 함수를 완성하시오.

### 제한 사항

- 1 ≤ ability의 행의 길이 = 학생 수 ≤ 10
- 1 ≤ ability의 열의 길이 = 종목 수 ≤ ability의 행의 길이
- 0 ≤ ability[i][j] ≤ 10,000
  - ability[i][j]는 i+1번 학생의 j+1번 종목에 대한 능력치를 의미합니다.

---
### Problem Solved Check
- [x] 1회 24/09/06
- [ ] 2회
- [ ] 3회

~~~
import itertools


def solution(ability):
    answer = 0
    for c in itertools.combinations(ability, len(ability[0])):
        score = return_max_score(c)
        answer = max(score, answer)
    return answer


def return_max_score(students):
    num = len(students)
    result = 0
    for p in itertools.permutations(range(num), num):
        score = 0
        for i in range(len(p)):
            score += students[i][p[i]]
        result = max(result, score)
    return result
    
~~~


