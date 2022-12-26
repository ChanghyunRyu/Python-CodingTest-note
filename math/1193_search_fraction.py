# 중요한 포인트는 x가 주어졌을 때, (x1, y1) 좌표 위치를 알아야한다는 것
x = int(input())
i = 0
while True:
    cal = i*(i+1)//2
    if cal >= x:
        break
    else:
        i += 1
dif = cal - x
co1 = i-dif
co2 = 1+dif
if i % 2 == 0:
    print('{}/{}'.format(co1, co2))
else:
    print('{}/{}'.format(co2, co1))
