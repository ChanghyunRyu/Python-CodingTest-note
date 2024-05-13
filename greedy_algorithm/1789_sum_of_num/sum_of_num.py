s = int(input())
n = 1
sum_of_num = 1
while True:
    n += 1
    sum_of_num += n
    if sum_of_num > s:
        break
print(n-1)
