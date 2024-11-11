import sys


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
r, c, m = map(int, input().split())
shark = {}


for _ in range(m):
    x1, y1, s, d, z = map(int, sys.stdin.readline().split())
    shark[(x1-1, y1-1)] = (s, d, z)


def move_shark(point, sp, di):
    x, y = point
    if di == UP or di == DOWN:
        cycle = 2*r-2
        sp %= cycle
        while sp > 0:
            if di == UP:
                if x-sp > 0:
                    x -= sp
                    sp = 0
                else:
                    sp -= x
                    x = 0
                    di = DOWN
            else:
                if x+sp < r:
                    x += sp
                    sp = 0
                else:
                    sp -= r-1-x
                    x = r-1
                    di = UP
    else:
        cycle = 2*c-2
        sp %= cycle
        while sp > 0:
            if di == RIGHT:
                if y+sp < c:
                    y += sp
                    sp = 0
                else:
                    sp -= c-1-y
                    y = c - 1
                    di = LEFT
            else:
                if y-sp > 0:
                    y -= sp
                    sp = 0
                else:
                    sp -= y
                    y = 0
                    di = RIGHT
    return (x, y), di


now = 0
answer = 0
while now < c:
    for i in range(r):
        if (i, now) in shark:
            answer += shark[(i, now)][2]
            del shark[(i, now)]
            break
    now += 1
    new_shark = {}
    for key in shark:
        speed, direction, size = shark[key]
        new_p, new_d = move_shark(key, speed, direction)
        if new_p not in new_shark:
            new_shark[new_p] = (speed, new_d, size)
        elif new_shark[new_p][2] < size:
            new_shark[new_p] = (speed, new_d, size)
    shark = new_shark
print(answer)
