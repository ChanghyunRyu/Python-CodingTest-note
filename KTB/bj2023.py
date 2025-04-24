n = int(input())

prime_number = {}
dp = [[] for _ in range(n+1)]
dp[1] = [2, 3, 5, 7]


def check_prime(num):
    if num == 2:
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(2, n+1):
    for num in dp[i-1]:
        base = 10 * num
        for j in range(1, 10):
            temp = base+j
            if check_prime(temp):
                dp[i].append(temp)


for answer in dp[n]:
    print(answer)
