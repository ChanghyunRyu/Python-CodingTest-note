n, m = map(int, input().split())

pledge = 0
for i in range(1, max(n, m)+1):
    if n % i == 0 and m % i == 0:
        pledge = i

multiple = n*m//pledge

print(pledge)
print(multiple)
