def solution(number, k):
    count = k
    stack = []
    for i in range(len(number)):
        while stack and count > 0 and int(stack[-1]) < int(number[i]):
            count -= 1
            stack.pop()
        if len(stack) < len(number)-k:
            stack.append(number[i])
    answer = ''.join(stack)
    return answer


# print(solution('1924', 2))
# print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('9876543214', 4))
