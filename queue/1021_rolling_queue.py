import time

n, m = map(int, input().split())
target = list(map(int, input().split()))
nums = [i+1 for i in range(n)]
# index = 현재 위치, count = 출력, 이동 횟수
index = 0
count = 0
for t in target:
    # 현재 위치 타겟 존재 확인
    if nums[index] == t:
        nums[index] = -1
        r = 0
        while (nums[index] == -1) & (r < n):
            index = (index+1) % n
            r += 1
        continue
    # 왼쪽 탐색, 오른쪽 탐색
    idx_left = index
    idx_right = index
    count_left = 0
    count_right = 0
    flag_left, flag_right = True, True
    while flag_left | flag_right:
        # 왼쪽 이동
        if flag_left:
            idx_left = (idx_left - 1) % n
            if nums[idx_left] != -1:
                count_left += 1
                if nums[idx_left] == t:
                    flag_left = False
        # 오른쪽 이동
        if flag_right:
            idx_right = (idx_right+1) % n
            if nums[idx_right] != -1:
                count_right += 1
                if nums[idx_right] == t:
                    flag_right = False
    count += min(count_right, count_left)
    index = idx_left
    nums[index] = -1
    r = 0
    while (nums[index] == -1) & (r < n):
        index = (index + 1) % n
        r += 1
print(count)
