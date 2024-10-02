def solution(number, k):
    stack = []
    count = 0
    for num in number:
        if not stack:
            stack.append(num)
            continue
        while stack and int(stack[-1]) < int(num) and count < k:
            stack.pop()
            count += 1
        stack.append(num)
    while count < k:
        count += 1
        stack.pop()
    return ''.join(stack)


print(solution('1924', 2))
print(solution("1231234", 3))
print(solution('4177252841', 4))
print(solution('9876543214', 4))
