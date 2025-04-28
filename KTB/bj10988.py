word = input()


def check_palindrome(w):
    for i in range(len(w)):
        if w[i] != w[-(i+1)]:
            return False
    return True


print('{}'.format(1 if check_palindrome(word) else 0))
