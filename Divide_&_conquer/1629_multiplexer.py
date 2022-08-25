# 나머지 구하는 부분까지는 맞는거 같음
a, b, c = map(int, input().split())


def multiplex(count):
    global a, c
    if count == 1:
        return a % c
    temp = multiplex(count // 2)
    if count % 2 == 0:
        return (temp*temp) % c
    else:
        return (temp * temp * a) % c


print(multiplex(b))
