def solution(s, n):
    answer = ''
    for ch in s:
        num_ch = ord(ch)
        if 65 <= num_ch <= 90:
            start = 65
            num_ch = ((num_ch-start+n) % 26)+start
        elif 97 <= num_ch <= 127:
            start = 97
            num_ch = ((num_ch - start + n) % 26) + start
        answer = ''.join([answer, chr(num_ch)])
    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
