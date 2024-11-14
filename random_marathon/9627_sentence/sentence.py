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
