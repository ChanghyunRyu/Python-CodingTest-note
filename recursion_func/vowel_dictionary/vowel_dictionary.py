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


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
