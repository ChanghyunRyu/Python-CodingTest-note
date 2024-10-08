## 스킬 트리

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/49993

선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 
썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 
가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

### 제한 사항

- 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
- 스킬 순서와 스킬트리는 문자열로 표기합니다.
  - 예를 들어, C → B → D 라면 "CBD"로 표기합니다
- 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
- skill_trees는 길이 1 이상 20 이하인 배열입니다.
- skill_trees의 원소는 스킬을 나타내는 문자열입니다.
  - skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

---
### Problem Solved Check
- [x] 1회 24/07/23
- [x] 2회 24/10/08
- [ ] 3회
~~~
def solution(skill, skill_trees):
    answer = 0
    dictionary = skill_to_num(skill)
    for skilltree in skill_trees:
        if check_skilltree(dictionary, skilltree):
            answer += 1
    return answer


def check_skilltree(dictionary, skill_tree):
    now_step = 0
    for skill in skill_tree:
        if skill in dictionary:
            if dictionary[skill] == now_step:
                now_step += 1
            else:
                return False
    return True


def skill_to_num(skill):
    result = {}
    for i in range(len(skill)):
        result[skill[i]] = i
    return result
    
~~~
