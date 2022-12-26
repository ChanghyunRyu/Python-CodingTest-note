n = int(input())
coordinates = []
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
coordinates = sorted(coordinates, key= lambda coo: (coo[1], coo[0]))
for coor in coordinates:
    print('{} {}'.format(coor[0], coor[1]))
