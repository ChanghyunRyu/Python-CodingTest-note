def solution(n):
    answer = 0

    # 3진법 변환
    divisor = 3
    temp = []
    while True:
        quotient = n//divisor
        remainder = n % divisor
        n = quotient
        temp.append(remainder)
        if n < 3:
            if quotient > 0:
                temp.append(n)
            break

    # 역수로 10진법 변환
    temp.reverse()
    for i in range(len(temp)):
        answer += (3**i)*temp[i]
    return answer


print(solution(45))
print(solution(125))
print(solution(1))
