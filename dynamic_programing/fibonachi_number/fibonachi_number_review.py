def solution(n):
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n] % 1234567


print(solution(3))
print(solution(5))
