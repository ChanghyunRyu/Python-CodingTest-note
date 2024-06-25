def solution(n):
    f_num = [0]*(n+1)
    f_num[1] = 1
    for i in range(2, n+1):
        f_num[i] = (f_num[i-1]+f_num[i-2])%1234567
    answer = f_num[-1]
    return answer
