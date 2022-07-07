answer = []
while True:
    x, y, z = map(int, input().split())
    if x == y and y == z and z == 0:
        break
    arr = [x, y, z]
    arr.sort(reverse=True)
    max_length = arr[0]
    x1, x2 = arr[1], arr[2]
    if (x1*x1) + (x2*x2) == max_length*max_length:
        answer.append('right')
    else:
        answer.append('wrong')
for ans in answer:
    print(ans)
