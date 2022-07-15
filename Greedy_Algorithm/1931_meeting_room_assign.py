# 시행착오가 많았던 문제
# ** 그리디 알고리즘을 사용하기 위한 정렬 방법의 선택이 잘못되었음.
# 1. 회의의 시작 순서가 빠른 순서로 채워나감 => 시작을 빨리 했다고 꼭 빨리 끝난다는 보장이 없음
# 2. 회의시간이 짧은 순서로 채워나감 => 회의 시간이 짧은 것을 "먼저" 선정할 경우, 회의 시간을 많이 사용하지만 딱 떨어지는 경우를 생각 x
# 3. 회의 종료 시간이 앞서는 순서 => 정답에 사용한 방법, 회의 종료가 빨리 된다는 것은 그 앞 공간을 가장 잘 사용했다는 것이 된다.
# 생각 못 했던 점: 회의 종료 시간순으로 정렬하 되, 시작시간 기준까지 넣지 않은 경우 오류가 발생할 수 있음.
import sys

n = int(input())
meetings = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))
count = start = 0
for meeting in meetings:
    if start <= meeting[0]:
        count += 1
        start = meeting[1]
print(count)
