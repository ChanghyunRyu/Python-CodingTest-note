def solution(brown, yellow):
    x_plus_y = brown//2+2
    for i in range(1, x_plus_y):
        x = i
        y = x_plus_y-i
        if x*y == brown+yellow:
            answer = [y, x]
            break
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
