def solution(brown, yellow):
    answer = []
    x_plus_y = brown//2 + 2
    x_mul_y = brown+yellow
    for i in range(1, x_plus_y):
        x, y = i, x_plus_y-i
        if x*y == x_mul_y:
            answer.append(x)
            answer.append(y)
            break
    answer.sort(reverse=True)
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
