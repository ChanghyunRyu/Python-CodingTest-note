t = int(input())


def check_group_word(w):
    check = {}
    before = ""
    for character in w:
        if before != character:
            if character in check:
                return False
            else:
                check[character] = 1
        before = character
    return True


answer = 0
for _ in range(t):
    word = input()
    if check_group_word(word):
        answer += 1
print(answer)
