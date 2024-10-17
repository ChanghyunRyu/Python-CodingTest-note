def solution(prices):
    s = []
    answer = [0]*(len(prices))
    for i in range(len(prices)):
        price = prices[i]
        if not s:
            s.append((price, i))
            continue
        while s and s[-1][0] > price:
            _, idx = s.pop()
            answer[idx] = i-idx
        s.append((price, i))
    while s:
        _, idx = s.pop()
        answer[idx] = len(prices)-idx-1
    answer[-1] = 0
    answer[-2] = 1
    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([5, 8, 6, 2, 4, 1]))
