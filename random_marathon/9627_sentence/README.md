## 9627번 문장

---

시간 제한: 1초, 메모리 제한: 128MB

옛날 옛적에 수학을 공부하는 사람들만 사는 나라가 있었다. 이 나라에 살고있는 상근이와 창영이는 자명한 문장에 대해서 토론을 하고 있었다.

자명한 문장에는 숫자를 하나만 포함하고 있으며, 그 숫자는 문장을 이루는 글자의 개수와 같다. 예를 들면, "This sentence has thirtyone letters.”, “Blah blah seventeen”과 같다.

상근이는 창영이에게 자명한 문장에서 숫자만 지운 문장을 주었다. 창영이는 가장 작은 수를 문장에 넣어 올바른 자명한 문장을 만드는 프로그램을 작성하려고 한다.

문장은 word1 word2 word3 ... $ word_n-1 word_n과 같은 형식으로 이루어져 있고, $는 숫자를 넣을 곳을 나타낸다.

예를 들어, 상근이는 “this sentence has thirtyone letters”를 “this sentence has $ letters”로 바꾸어 창영이에게 전달해준다.

숫자는 다음과 같은 규칙을 지키면서 써야한다.

- 1부터 10까지 숫자는 “one”, “two”, “three”, “four”, “five”, “six”, “seven”, “eight”, “nine”, “ten”로 쓴다.
- 11부터 19까지 숫자는 “eleven”, “twelve”, “thirteen”, “fourteen”, “fifteen”, “sixteen”, “seventeen”, “eighteen”, “nineteen”로 쓴다.
- 나머지 두 자리 숫자는 십의 자리를 쓰고 일의 자리를 쓴다. 만약 일의 자리가 0인 경우에는 십의 자리만 쓴다.
- 십의 자리의 경우에 2부터 9까지는 “twenty”, “thirty”, “forty”, “fifty”, “sixty”, “seventy”, “eighty”, “ninety”로 쓴다.
- 세 자리 숫자는 백의 자리를 쓰고, 나머지 두 자리를 쓴다. 두 자리가 0인 경우에는 백의 자리만 쓰면 된다.
- 백의 자리의 경우에 1부터 9까지는 “onehundred”, “twohundred”, “threehundred”, “fourhundred”, “fivehundred”, “sixhundred”, “sevenhundred”, “eighthundred”, “ninehundred”로 쓴다.
- 항상 세자리 이내로 문제를 풀 수 있다.

### 입력

- 첫째 줄에 문장을 이루는 단어의 수 N (1 ≤ N ≤ 20)가 주어진다.
- 다음 N개 줄에는 문장을 이루는 단어가 주어진다. 입력으로 주어지는 단어는 길이가 최대 50이며 알파벳 소문자로만 이루어져 있다. 입력으로 주어지는 단어 중에 숫자를 나타내는 단어는 없다.
- $는 하나만 주어진다.

### 출력

- 첫째 줄에 문장을 출력한다. 항상 답이 존재하는 경우만 주어지며, 숫자는 항상 1000보다 작다.

---
### Problem Solved Check
- [x] 1회 24/11/14
- [ ] 2회
- [ ] 3회
~~~
n = int(input())
letters = 0
answer = []
for _ in range(n):
    word = input()
    answer.append(word)
    if word != '$':
        letters += len(word)

number = [0]*1000
word = ['']*1000
word[1:19] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
temp = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
for i in range(2, 10):
    word[i*10] = temp[i-2]
for i in range(100):
    if word[i] != '':
        number[i] = len(word[i])


def get_number_len(num):
    if number[num] != 0 or num == 0:
        return number[num]
    if num >= 100:
        hundred = num//100
        return get_number_len(hundred)+len('hundred')+get_number_len(num % 100)
    else:
        ten = (num//10)*10
        one = num % 10
        return get_number_len(ten)+get_number_len(one)


def number_to_word(num):
    if word[num] != '':
        return word[num]
    if num > 100:
        hundred = num//100
        return number_to_word(hundred)+'hundred'+number_to_word(num % 100)
    ten = (num//10)*10
    one = num % 10
    return number_to_word(ten)+number_to_word(one)


result = 0
for i in range(1, 1000):
    if letters+get_number_len(i) == i:
        result = i
        break

for w in answer:
    if w != '$':
        print(w, end=' ')
    else:
        print(number_to_word(result), end=' ')

~~~