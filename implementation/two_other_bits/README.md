## 2개 이하의 다른 비트

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/77885

양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.
- x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

정수들이 담긴 배열 numbers가 매개변수로 주어집니다. 
numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

---
### Problem Solved Check
- [x] 1회  24/07/19
- [x] 2회  24/10/07
- [ ] 3회
~~~
def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(find_2bits(n))
    return answer


def find_2bits(number):
    bits_number = ten_to_two(number)
    result = bits_number
    if bits_number[0] == 0:
        result[0] = 1
        return two_to_ten(result)
    for i in range(1, len(bits_number)):
        if bits_number[i] == 0 and bits_number[i-1] == 1:
            result[i] = 1
            result[i-1] = 0
            return two_to_ten(result)
    

def ten_to_two(number):
    result = []
    while number >= 2:
        result.append(number % 2)
        number = number//2
    result.append(number)
    result.append(0)
    return result


def two_to_ten(number):
    result = 0
    for i in range(len(number)):
        result += number[i]*(2**i)
    return result
    
~~~