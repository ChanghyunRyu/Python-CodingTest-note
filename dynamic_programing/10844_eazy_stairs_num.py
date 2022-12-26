n = int(input())
result = [0] + [1]*9

for i in range(1, n):
    temp = list(result)
    result[0] = temp[1]
    result[9] = temp[8]
    for j in range(1, 9):
        result[j] = temp[j-1] + temp[j+1]
score = 0
for num in result:
    score += num % 1000000000
print(score % 1000000000)
