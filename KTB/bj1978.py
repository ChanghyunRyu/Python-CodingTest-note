n = int(input())
nums = list(map(int, input().split()))


def check_prime_number(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


answer = 0
for n in nums:
    if check_prime_number(n):
        answer += 1
print(answer)
