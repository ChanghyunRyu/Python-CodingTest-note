import sys

n = int(input())
arr = []
numbers = [0]*8001
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    arr.append(num)
    numbers[num + 4000] += 1

arr.sort()
mean = round(sum(arr)/n)

median = arr[n//2]

max_frequency_arr = []
max_frequency = 0
for idx in range(len(numbers)):
    if max_frequency < numbers[idx]:
        max_frequency = numbers[idx]
        max_frequency_arr = [idx-4000]
    elif max_frequency == numbers[idx]:
        max_frequency_arr.append(idx-4000)
max_frequency_arr.sort()

r = arr[n-1] - arr[0]
print(mean)
print(median)
if len(max_frequency_arr) == 1:
    print(max_frequency_arr[0])
else:
    print(max_frequency_arr[1])
print(r)
