def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]
    while stack:
        now, idx = stack.pop()
        if idx == len(numbers)-1:
            if now+numbers[idx] == target or now-numbers[idx] == target:
                answer += 1
            continue
        stack.append((now+numbers[idx], idx+1))
        stack.append((now-numbers[idx], idx+1))
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
