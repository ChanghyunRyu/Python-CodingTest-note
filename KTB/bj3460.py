def ten_2_bi(num):
    result = []
    while num >= 2:
        remain = num % 2
        num = num // 2
        result.append(remain)
    if num == 1:
        result.append(num)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    temp = ten_2_bi(n)
    answer = []
    for i in range(len(temp)):
        if temp[i] == 1:
            answer.append(str(i))
    print(' '.join(answer))
