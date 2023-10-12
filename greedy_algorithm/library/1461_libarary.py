n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr_minus = [0]
arr_plus = [0]

for a in arr:
    if a < 0:
        arr_minus.append(a)
    else:
        arr_plus.append(a)
arr_minus.sort()
arr_plus.sort(reverse=True)

count = 0
i = 0

while i < len(arr_minus):
    count -= arr_minus[i]*2
    i += m
i = 0
while i < len(arr_plus):
    count += arr_plus[i]*2
    i += m
count -= max(abs(arr_minus[0]), abs(arr_plus[0]))
print(count)
