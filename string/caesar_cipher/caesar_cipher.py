def solution(s, n):
    answer = ''
    for ch in s:
        num_ch = ord(ch)
        if ord('a') <= num_ch <= ord('z'):
            start = ord('a')
        elif ord('A') <= num_ch <= ord('Z'):
            start = ord('A')
        num_ch = ((num_ch - start + n) % 26) + start
        answer = ''.join([answer, chr(num_ch)])
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
