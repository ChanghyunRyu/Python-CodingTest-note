import sys

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(map(int, sys.stdin.readline().split())))

price_red = [0]*n
price_green = [0]*n
price_blue = [0]*n
price_red[0], price_green[0], price_blue[0] = paint[0][0], paint[0][1], paint[0][2]

for i in range(1, n):
    price_red[i] = min(price_blue[i-1], price_green[i-1]) + paint[i][0]
    price_green[i] = min(price_red[i-1], price_blue[i-1]) + paint[i][1]
    price_blue[i] = min(price_red[i-1], price_green[i-1]) + paint[i][2]

print(min(price_red[n-1], price_green[n-1], price_blue[n-1]))
