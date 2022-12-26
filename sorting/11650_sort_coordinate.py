# 조건을 설정하는 파이썬의 기본 정렬 함수 사용법 다시 상기
n = int(input())
coordinates = []
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates = sorted(coordinates, key = lambda coo: (coo[0], coo[1]))
for coor in coordinates:
    print('{} {}'.format(coor[0], coor[1]))
