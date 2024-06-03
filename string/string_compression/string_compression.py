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


print(solution("abcabcdede"))
print(solution('aaaaaaaaaabbbbbbbbbb'))
