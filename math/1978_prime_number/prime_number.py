n = int(input())
nums = list(map(int, input().split()))

prime_number = {}
limit = max(nums)
for i in range(2, limit+1):
    is_prime = True
    for p in prime_number:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        prime_number[i] = True

count = 0
for n in nums:
    if n in prime_number:
        count += 1

print(count)
