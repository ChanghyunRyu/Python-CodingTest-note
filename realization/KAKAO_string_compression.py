# 실패1: 문자열이 1인 경우를 생각하지 못 했다.
# 실패2: 자주하는 실수인데 배열의 끝일 때를 생각하지 못해 마지막만 빼놓고 돌아가는 경우를 더러 발생시키는 듯하다.
# 아쉬운 점: 문자열을 원하는 단위로 나누는 작업이 매끄럽지 못 했다.
sentence = input()


def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    for n in range(1, int(len(s)//2)+1):
        char_list = [s[i*n:(i+1)*n] for i in range((len(s)+n-1)//n)]
        char_list.append('')
        result = []
        before_word = ''
        word_count = 1
        for char in char_list:
            if char == before_word:
                word_count += 1
            else:
                if word_count == 1:
                    result.append(before_word)
                else:
                    result.append(str(word_count)+before_word)
                word_count = 1
            before_word = char
        result = ''.join(result)
        result_len = len(result)
        if answer == 0 or answer > result_len:
            answer = result_len
    return answer


print(solution(sentence))
