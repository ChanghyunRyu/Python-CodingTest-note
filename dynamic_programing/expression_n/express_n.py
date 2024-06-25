def solution(n, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        now = dp[i]
        now.add(int(str(n) * i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    now.add(k+l)
                    if k-l > 0:
                        now.add(k-l)
                    now.add(k*l)
                    if k != 0 and l != 0:
                        now.add(k//l)
        if number in now:
            return i
    return -1


print(solution(5, 5))
