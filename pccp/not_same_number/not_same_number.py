def solution(arr):
    stack = []
    for num in arr:
        if not stack:
            stack.append(num)
        elif stack[-1] == num:
            continue
        else:
            stack.append(num)
    return stack