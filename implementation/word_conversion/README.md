## 단어 변환

---

두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
~~~
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
~~~

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 
return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0를 return 합니다.

---
### Problem Solved Check
- [x] 1회 24/08/12
- [ ] 2회
- [ ] 3회
~~~
def solution(begin, target, words):
    answer = 0
    dp = {}
    count = 0
    dp[0] = {begin}
    all_word = {begin}
    before_word_len = len(begin)

    while True:
        word_list = dp[count]
        new_set = set()
        for word in word_list:
            conversion_word(word, words, new_set)
        count += 1
        dp[count] = new_set
        if target in dp[count]:
            answer = count
            break
        all_word = all_word.union(new_set)
        if len(all_word) == before_word_len:
            break
        before_word_len = len(all_word)
    return answer


def check_word(word, target):
    count = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            count += 1
            if count > 1:
                return False
    if count == 1:
        return True
    return


def conversion_word(begin, word_list, word_set):
    for word in word_list:
        if check_word(word, begin):
            word_set.add(word)
            
~~~
