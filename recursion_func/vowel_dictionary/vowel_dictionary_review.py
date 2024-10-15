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


print(solution("AAAAE"))
print(solution('AAAE'))
print(solution('I'))
