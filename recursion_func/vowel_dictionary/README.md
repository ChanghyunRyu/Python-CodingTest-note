## 모음 사전

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/84512

사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 
길이 5 이하의 모든 단어가 수록되어 있습니다. 
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 
이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- word의 길이는 1 이상 5 이하입니다.
- word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

---
### Problem Solved Check
- [x] 1회 24/06/10
- [x] 2회 24/10/15
- [ ] 3회

~~~
def solution(word):
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(len(word)):
        num = dic[word[i]]
        answer += calc_before_word(num, i)
        answer += 1
    return answer


def calc_before_word(n, index):
    result = 0
    if n == 0:
        return result
    for i in range(5 - index):
        result += 5**i
    result *= n
    return result
    
~~~
~~~
def solution(word):
    dictionary = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(len(word)):
        answer += 1
        temp = 0
        for j in range(5-i):
            temp += 5**j
        answer += dictionary[word[i]]*temp
    return answer
    
~~~
