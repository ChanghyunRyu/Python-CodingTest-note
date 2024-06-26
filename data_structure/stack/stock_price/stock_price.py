def solution(prices):
    answer = [0]*len(prices)
    stack = [(prices[-1], 0)]
    for i in range(len(prices)-2, -1, -1):
        now_price = prices[i]
        count = 1
        while stack and now_price <= stack[-1][0]:
            price, period = stack.pop()
            count += period
        stack.append((now_price, count))
        answer[i] = count
    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([5, 8, 6, 2, 4, 1]))
