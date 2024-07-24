## 문자열 압축

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/60057

데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 
표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

### 제한 사항
- s의 길이는 1 이상 1,000 이하입니다.
- s는 알파벳 소문자로만 이루어져 있습니다.

---
### Problem Solved Check
- [x] 1회 24/06/03
- [x] 2회 24/07/24
- [ ] 3회

문제 해결 접근 자체는 잘 했으나, 
문자열 반복이 9->10, 99->100 등으로 늘어나는 경우 문자열 길이가 달라진다는 것을 생각하지 못 했다.

~~~
import math


def solution(s):
    answer = len(s)
    word_count = 1
    while word_count <= len(s)//2:
        length = 0
        before_word = ''
        count = 0
        for i in range(math.ceil(len(s)/word_count)):
            # 현재 끊은 단어 구하기
            if (i+1)*word_count < len(s):
                now_word = s[i*word_count: (i+1)*word_count]
            else:
                now_word = s[i*word_count:]
            if before_word == now_word:
                count += 1
                if count == 2 or len(str(count-1)) != len(str(count)):
                    length += 1
            else:
                length += len(now_word)
                before_word = now_word
                count = 1
        answer = min(answer, length)
        word_count += 1
    return answer
~~~
~~~
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        tmp_length = compress_string(s, i)
        if answer > tmp_length:
            answer = tmp_length
    return answer


def compress_string(s, interval):
    temp = []
    before_token = s[:interval]
    count = 1
    for i in range(interval, len(s), interval):
        end = i+interval
        if i+interval >= len(s):
            end = len(s)

        if before_token == s[i:end]:
            count += 1
        else:
            if count == 1:
                temp.append(before_token)
            else:
                temp.append('{}{}'.format(count, before_token))
            before_token = s[i:end]
            count = 1
    if count == 1:
        temp.append(before_token)
    else:
        temp.append('{}{}'.format(count, before_token))
    s = ''.join(temp)
    return len(s)
~~~
