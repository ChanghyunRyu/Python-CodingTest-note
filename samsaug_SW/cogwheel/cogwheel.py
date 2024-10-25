
wheel = []
for _ in range(4):
    wheel.append(list(map(int, input())))

k = int(input())
rolls = []
for _ in range(k):
    rolls.append(map(int, input().split()))

wheel_left = [6]*4
wheel_right = [2]*4


def wheel_roll(number, direction, check):
    check[number] = True
    if number-1 >= 0 and not check[number-1] and wheel[number-1][wheel_right[number-1]] != wheel[number][wheel_left[number]]:
        wheel_roll(number-1, -direction, check)
    if number+1 < 4 and not check[number+1] and wheel[number+1][wheel_left[number+1]] != wheel[number][wheel_right[number]]:
        wheel_roll(number+1, -direction, check)
    wheel_right[number] = (wheel_right[number]-direction) % 8
    wheel_left[number] = (wheel_left[number]-direction) % 8


for num, d in rolls:
    wheel_roll(num-1, d, [False]*4)

answer = 0
for i in range(4):
    top = (wheel_right[i]-2) % 8
    answer += 2**i * wheel[i][top]
print(answer)
