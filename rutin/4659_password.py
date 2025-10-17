vowel = {'a': 1, 'e': 1, 'i': 1, 'o': '1', 'u': 1}


def check_pw(pw):
    check_vowel = pw[0] in vowel
    was_vowel = pw[0] in vowel
    count = 1
    last_char = pw[0]
    if len(pw) == 1:
        return check_vowel
    for i in range(1, len(pw)):
        if last_char == pw[i] and last_char != 'e' and last_char != 'o':
            return False
        if pw[i] in vowel:
            check_vowel = True
            if was_vowel:
                count += 1
            else:
                count = 1
                was_vowel = True
        else:
            if was_vowel:
                count = 1
                was_vowel = False
            else:
                count += 1
        if count >= 3:
            return False
        last_char = pw[i]
    return check_vowel


test_case = []
temp = ''
while True:
    temp = input()
    if temp == 'end':
        break
    test_case.append(temp)

for t in test_case:
    if check_pw(t):
        print('<{}> is acceptable.'.format(t))
    else:
        print('<{}> is not acceptable.'.format(t))
