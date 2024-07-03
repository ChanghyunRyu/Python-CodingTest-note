## 보석 쇼핑

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/67258

개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 
이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 
이전처럼 진열대의 특정 범위의 보석을 모두 구매하되 특별히 아래 목적을 달성하고 싶었습니다.

~~~
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
~~~

### 제한 사항

- gems 배열의 크기는 1 이상 100,000 이하입니다.
  - gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
  - gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
  - gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.

--
### Problem Solved Check
- [ ] 1회 
- [ ] 2회
- [ ] 3회
~~~
def solution(gems):
    answer = [0, len(gems) - 1]
    kind = len(set(gems))

    gems_dict = {gems[0]: 1}
    start = end = 0
    while end < len(gems):
        if len(gems_dict) < kind:
            end += 1
            if end >= len(gems):
                break
            if gems[end] not in gems_dict:
                gems_dict[gems[end]] = 1
            else:
                gems_dict[gems[end]] += 1
        else:
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer
    
~~~
