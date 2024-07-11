def find_window(number):
    num = 1
    answer = 0
    while num*num <= number:
        answer += 1
        num += 1
    return answer


n = int(input())
print(find_window(n))
