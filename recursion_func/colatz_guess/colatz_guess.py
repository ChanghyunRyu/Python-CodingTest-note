count = 0


def solution(num):
    global count
    if num == 1:
        return count
    count += 1
    if count >= 500:
        return -1
    if num % 2 == 0:
        return solution(num//2)
    else:
        return solution((num*3)+1)


print(solution(16))

