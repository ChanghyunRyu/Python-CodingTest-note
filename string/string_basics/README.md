## 문자열 다루기 기본

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/12918

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

### 제한 사항

- s는 길이 1 이상, 길이 8 이하인 문자열입니다.
- s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

---
### Problem Solved Check
- [x] 1회 24/06/05
- [x] 2회 24/07/27
- [ ] 3회

역시 파이썬 내장함수에 대한 지식이 있으면 쉽게 풀 수 있다.

- isdigit(): 숫자인지 판단하는 함수

~~~
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for char in s:
        if not char.isdigit():
            return False
    return True

~~~

책에서는 해당 문제를 정규표현식으로 푸는 방법 역시 제공하므로 해당 풀이로 풀어보았다.  
해당 풀이는 정규표현식을 한 번 보고 오는 것이 좋다.

~~~
import re


def solution(s):
    if (len(s) == 4 or len(s) == 6) and re.match('^\d*$', s):
        return True
    return False
~~~
