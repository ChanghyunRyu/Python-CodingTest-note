# 속도를 생각하면 계수정렬이 맞다고 생각
# 범위 -4000 ~ 4000 = 8001개, 각 수는 index-4000
import sys

n = int(input())
numbers = [0]*8001
for i in range(n):
    numbers[int(sys.stdin.readline())+4000] += 1

# 1,2,2,3,4
total = 0
count = 0
middle = (n//2) + 1
max_frequency = 0
max_frequency_num = []
min_num = 4001
max_num = -4001
for i in range(len(numbers)):
    total += (i-4000)*numbers[i]
    if count < middle <= (count + numbers[i]):
        median = i-4000
    count += numbers[i]
    if max_frequency < numbers[i]:
        max_frequency = numbers[i]
        max_frequency_num = [i-4000]
    elif max_frequency == numbers[i]:
        max_frequency_num.append(i-4000)
    if not numbers[i] == 0:
        if min_num > (i-4000):
            min_num = i-4000
        if max_num < (i-4000):
            max_num = i-4000
print(int(round(total/n, 0)))
print(median)
if len(max_frequency_num) > 1:
    max_frequency_num.sort()
    print(max_frequency_num[1])
else:
    print(max_frequency_num[0])
print(max_num-min_num)
