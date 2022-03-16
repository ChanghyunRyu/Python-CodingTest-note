# 실수 - 배열 만들어서 계산하는데 처음에 range(n)으로 해서 전체적으로 꼬였음.
# 해당 코드대로라면 이런 식이 아니라 n+1로 해야 됨. 배열 인덱스에 대한 실수를 자주 한다.
n = int(input())
collect_arr = [0 for i in range(n+1)]
for num in range(n+1):
    if num == 0 or num == 1:
        continue
    collect_arr[num] = collect_arr[num-1]+1
    if num % 2 == 0:
        if collect_arr[num] > (collect_arr[num//2] + 1):
            collect_arr[num] = collect_arr[num//2] + 1
    if num % 3 == 0:
        if collect_arr[num] > (collect_arr[num//3] + 1):
            collect_arr[num] = collect_arr[num//3] + 1
print(collect_arr[n])
