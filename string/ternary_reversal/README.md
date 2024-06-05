## 3진법 뒤집기

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/68935

자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- n은 1 이상 100,000,000 이하인 자연수입니다.

---
### Problem Solved Check
- [x] 1회 24/06/04
- [ ] 2회
- [ ] 3회

~~~
def solution(n):
    answer = 0

    # 3진법 변환
    divisor = 3
    temp = []
    while True:
        quotient = n//divisor
        remainder = n % divisor
        n = quotient
        temp.append(remainder)
        if n < 3:
            if quotient > 0:
                temp.append(n)
            break
            
    # 역수로 10진법 변환
    temp.reverse()
    for i in range(len(temp)):
        answer += (3**i)*temp[i]
    return answer
~~~
