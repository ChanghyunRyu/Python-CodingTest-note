# 백준 2839 설탕 배달 문제
n = int(input())
count = -1
five_num = n//5
if n % 5 == 0:
    count = five_num
else:
    for i in reversed(range(five_num+1)):
        if (n-(i*5)) % 3 == 0:
            count = int(i + ((n-(i*5))/3))
            break
print(count)
