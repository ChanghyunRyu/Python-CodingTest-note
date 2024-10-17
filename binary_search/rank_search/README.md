## 순위 검색

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/72412

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info,  
개발팀이 궁금해하는 문의 조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,  
각 문의 조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

### 제한 사항

- info 배열의 크기는 1 이상 50,000 이하입니다.
- info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친 "개발언어 직군 경력 소울푸드 점수" 형식입니다.
  - 개발언어는 cpp, java, python 중 하나입니다.
  - 직군은 backend, frontend 중 하나입니다.
  - 경력은 junior, senior 중 하나입니다.
  - 소울푸드는 chicken, pizza 중 하나입니다.
  - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
- query 배열의 크기는 1 이상 100,000 이하입니다.
  - [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
  - 언어는 cpp, java, python, - 중 하나입니다.
  - 직군은 backend, frontend, - 중 하나입니다.
  - 경력은 junior, senior, - 중 하나입니다.
  - 소울푸드는 chicken, pizza, - 중 하나입니다.
  - '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
  - X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
  - 예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.

---
### Problem Solved Check
- [X] 1회 24/06/20 
- [X] 2회 24/08/06
- [ ] 3회

~~~
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    applicants = info_to_dict(info)
    for q in query:
        key, score = query_to_key(q)
        pass_applicant = applicants[key]
        number = len(pass_applicant) - bisect_left(pass_applicant, score)
        answer.append(number)
    return answer


def info_to_dict(info):
    result = defaultdict(list)
    for i in info:
        tokens = i.split()
        score = int(tokens.pop())
        result[''.join(tokens)].append(score)
        for j in range(4):
            cbi = combinations(tokens, j)
            for c in cbi:
                result[''.join(c)].append(score)
    for i in result:
        result[i].sort()
    return result


def query_to_key(query):
    tokens = query.split()
    score = tokens.pop()
    key = ''.join(tokens)
    key = key.replace('and', '').replace(' ', '').replace('-', '')
    return key, int(score)

~~~
bisect_left 사용법 숙지할 것!, 조건이 바뀔 수 있을 경우 해당 바뀌는 조건들을 모두 자료에 추가하는 방법 생각할 것!
~~~
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    result = []
    dictionary = info_to_dict(info)
    for q in query:
        temp = get_successful_candidates(q, dictionary)
        result.append(temp)
    return result


def info_to_dict(info):
    result = {}
    for applicant in info:
        tokens = applicant.split()
        insert_token_dict(tokens, result)
    for key in result:
        result[key].sort()
    return result


def insert_token_dict(tokens, dictionary):
    score = int(tokens[4])
    tokens = tokens[:4]
    for i in range(len(tokens)+1):
        for combination in combinations(tokens, i):
            key = ''.join(combination)
            if key in dictionary:
                dictionary[key].append(score)
            else:
                dictionary[key] = [score]


def get_successful_candidates(query, dictionary):
    tokens = query.split()
    score = int(tokens[len(tokens)-1])
    tokens = tokens[:len(tokens)-1]
    temp = []
    for token in tokens:
        if token == '-' or token == 'and':
            continue
        else:
            temp.append(token)
    final_query = ''.join(temp)
    if final_query in dictionary:
        applicants = dictionary[final_query]
        result = len(applicants) - bisect_left(applicants, score)
    else:
        result = 0
    return result
    
~~~