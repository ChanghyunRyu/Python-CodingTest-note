# 틀렸던 부분: 이분 탐색을 할 경우, 범위 선택을 너무 타이트하게 할 필요가 없다.
# 탐색 시간을 단축하고 싶어 탐색 범위를 최대한 줄이려고 했으나 정답이 들어있는 케이스를 버릴 수도 있다는 것을 망각했다.
import sys

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
# 탐색 범위는 가장 짧은 거리~가장 긴 거리
house.sort()
left, right = 1, house[n-1]-house[0]
result = 0
if c == 2:
    result = house[n-1]-house[0]
else:
    while left <= right:
        mid = (left + right) // 2
        router, start, target = 1, 0, 1
        # 해당 길이 이상 공유기 설치할 수 있는지 확인
        while target < n and router < c:
            if house[target] - house[start] < mid:
                target += 1
            else:
                router += 1
                start = target
                target += 1
        # 설치한 공유기 c보다 많으면 조건을 충족, 이보다 큰 수가 있는지 탐색
        if router >= c:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
print(result)

