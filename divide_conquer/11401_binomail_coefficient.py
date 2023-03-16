# (n!/ k!(n-k)!) %p = n! % p * ((k!(n-k)!)^p-2) % p
n, k = map(int, input().split())
mod = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a, b // 2) ** 2 * a) % mod
    else:
        return (power(a, b//2) ** 2) % mod


fact = [1 for _ in range(n+1)]
for i in range(2, n+1):
    fact[i] = fact[i-1] * i % mod

A = fact[n]
B = (fact[k] * fact[n-k]) % mod
result = ((A % mod) * (power(B, mod-2) % mod)) % mod
print(result)
