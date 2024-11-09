from collections import deque


n, k = map(int, input().split())
conveyor = list(map(int, input().split()))
start = 0
robots = deque()
broken = 0
count = 0

while broken < k:
    count += 1
    start = (start-1) % (2*n)
    new_robots = deque()
    check = {}
    while robots:
        robot = robots.popleft()
        # 내리는 위치 확인
        if (start+n-1) % (2*n) == robot:
            continue
        np = (robot+1) % (2*n)
        if np not in check and np != (start+n) % (2*n) and conveyor[np] > 0:
            conveyor[np] -= 1
            if (start + n - 1) % (2 * n) != np:
                new_robots.append(np)
                check[np] = 1
            if conveyor[np] == 0:
                broken += 1
        else:
            new_robots.append(robot)
            check[robot] = 1
    if conveyor[start] > 0:
        conveyor[start] -= 1
        new_robots.append(start)
        if conveyor[start] == 0:
            broken += 1
    robots = new_robots
print(count)
