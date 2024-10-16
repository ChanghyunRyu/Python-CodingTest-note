## 불량 사용자

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/64064

개발팀 내에서 이벤트 개발을 담당하고 있는 "무지"는 최근 진행된 카카오 이모티콘 이벤트에 
비정상적인 방법으로 당첨을 시도한 응모자들을 발견하였습니다. 
이런 응모자들을 따로 모아 불량 사용자라는 이름으로 목록을 만들어서 당첨 처리 시 제외하도록 
이벤트 당첨자 담당자인 "프로도" 에게 전달하려고 합니다.  
이 때 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달했습니다. 
가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용하였습니다.
"무지"와 "프로도"는 불량 사용자 목록에 매핑된 응모자 아이디를 제재 아이디 라고 부르기로 하였습니다.

### 제한 사항

- user_id 배열의 크기는 1 이상 8 이하입니다.
- user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
  - 응모한 사용자 아이디들은 서로 중복되지 않습니다.
  - 응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.
- banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.
- banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
  - 불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다. 
  - 불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
- 불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
- 제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.

---
### Problem Solved Check
- [x] 1회 24/06/14
- [x] 2회 24/10/16
- [ ] 3회

~~~
def solution(user_id, banned_id):
    stack = [([], 0, user_id)]
    result = []
    while stack:
        result_list, index, user_list = stack.pop()
        if index == len(banned_id):
            result_list.sort()
            if result_list not in result:
                result.append(result_list)
            continue
        for user in user_list:
            if check_id(banned_id[index], user):
                next_result_list = list(result_list)
                next_result_list.append(user)
                next_user_list = list(user_list)
                next_user_list.remove(user)
                stack.append((next_result_list, index+1, next_user_list))
    return len(result)


def check_id(ban_id, chk_id):
    if len(ban_id) != len(chk_id):
        return False
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        if ban_id[i] != chk_id[i]:
            return False
    return True
    
~~~
~~~
import itertools


def solution(user_id, banned_id):
    answer = set()
    for permutation in itertools.permutations(user_id, len(banned_id)):
        permutation = list(permutation)
        flag = True
        for i in range(len(permutation)):
            if not match_user_id(permutation[i], banned_id[i]):
                flag = False
                break
        if flag:
            answer.add(''.join(sorted(permutation)))
    return len(answer)


def match_user_id(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] == '*':
            continue
        if user_id[i] != banned_id[i]:
            return False
    return True
    
~~~