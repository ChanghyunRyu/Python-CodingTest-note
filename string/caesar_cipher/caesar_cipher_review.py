def solution(s, n):
    answer = []
    for i in s:
        answer.append(caesar_cipher(i, n))
    return ''.join(answer)


def caesar_cipher(character, num):
    result = ''
    if character == ' ':
        result = character
    if character.isupper():
        now_ord = ord(character)
        a_ord = ord('A')
        now_ord = (((now_ord + num)-a_ord) % 26) + a_ord
        result = chr(now_ord)
    if character.islower():
        now_ord = ord(character)
        a_ord = ord('a')
        now_ord = (((now_ord + num)-a_ord) % 26) + a_ord
        result = chr(now_ord)
    return result


print(solution("AB", 1))
print(solution('z', 1))
print(solution('a B z', 4))

