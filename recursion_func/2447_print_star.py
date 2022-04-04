# 1. 출력을 이용한 재귀함수 형태로는 풀이가 어려울 것 같다.
# NxN 만큼의 배열을 만들어서 하는 건 가능할까?
# 해결!
n = int(input())
stars = [[' '] * n for i in range(n)]


def writing_star(x, y, size):
    if size == 1:
        x = int(x)
        y = int(y)
        stars[x][y] = '*'
    else:
        writing_star(x, y, size / 3)
        writing_star(x + (size / 3), y, size / 3)
        writing_star(x + (2 * size / 3), y, size / 3)
        writing_star(x, y + (size / 3), size / 3)
        writing_star(x + (2 * size / 3), y + (size / 3), size / 3)
        writing_star(x, y + (2 * size / 3), size / 3)
        writing_star(x + (size / 3), y + (2 * size / 3), size / 3)
        writing_star(x + (2 * size / 3), y + (2 * size / 3), size / 3)


writing_star(0, 0, n)
for line in stars:
    for star in line:
        print(star, end='')
    print()
