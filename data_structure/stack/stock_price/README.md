## 주식 가격

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42584

n초 간의 주가를 초 단위로 기록한 배열 prices가 매개변수로 주어질 때, 
각 초의 주가를 기준으로 해당 초 부터 n초 사이에 가격이 떨어지지 않은 시간은 
몇 초인지 배열에 담아 return 하도록 solution 함수를 완성하세요.

### 제한 사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

---
### Problem Solved Check
- [x] 1회 24/06/26
- [x] 2회 24/10/17
- [ ] 3회

스택을 사용한다고 알고 풀어서 쉬운 문제 그 전 값과 비교하는 문제는 스택을 사용할 수 도 있다는 걸 염두에 두어야 할 것!!

~~~
def solution(prices):
    answer = [0]*len(prices)
    stack = [(prices[-1], 0)]
    for i in range(len(prices)-2, -1, -1):
        now_price = prices[i]
        count = 1
        while stack and now_price <= stack[-1][0]:
            price, period = stack.pop()
            count += period
        stack.append((now_price, count))
        answer[i] = count
    return answer
    
~~~
~~~
def solution(prices):
    s = []
    answer = [0]*(len(prices))
    for i in range(len(prices)):
        price = prices[i]
        if not s:
            s.append((price, i))
            continue
        while s and s[-1][0] > price:
            _, idx = s.pop()
            answer[idx] = i-idx
        s.append((price, i))
    while s:
        _, idx = s.pop()
        answer[idx] = len(prices)-idx-1
    answer[-1] = 0
    answer[-2] = 1
    return answer
    
~~~