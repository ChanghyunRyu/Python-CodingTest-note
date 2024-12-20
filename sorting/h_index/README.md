## H-Index

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42747

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

---
### Problem Solved Check
- [x] 1회 24/06/17
- [x] 2회 24/08/02
- [x] 3회 24/10/16
~~~
def solution(citations):
    answer = 0
    count = [0]*10001
    for citation in citations:
        count[citation] += 1
    sum_count = 0
    for i in range(len(count)-1, 0, -1):
        sum_count += count[i]
        if sum_count >= i:
            answer = i
            break
    return answer
~~~
~~~
def solution(citations):
    count = [0]*(max(citations)+1)
    for i in citations:
        count[i] += 1
    answer = 0
    prefix = [0]*len(count)
    prefix[len(prefix)-1] = count[len(count)-1]
    for i in range(len(count)-2, -1, -1):
        prefix[i] = prefix[i+1]+count[i]
        if prefix[i] >= i:
            answer = max(i, answer)
    return answer
    
~~~
실수: range(0, -1, -1)이면 아예 없음이 반환됨.
~~~
def solution(citations):
    h_index = [0]*10001
    for citation in citations:
        h_index[citation] += 1
    for i in range(max(citations)-1, -1, -1):
        h_index[i] += h_index[i+1]
        if h_index[i+1] >= i+1:
            return i+1
    return 0
~~~