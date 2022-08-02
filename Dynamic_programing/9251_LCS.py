# 0.1초를 요구하는 문제;;
# 각 문자를 하나씩 늘려주는 2차원 배열이라고 생각해야 한다.
# 그 전에 했던 전봇대 문제를 이용하여 풀려했으나 해당 사항의 경우, 시간초과가 일어남
# 두 방향으로 나아갈 수 있다는 것을 생각했어야 했음.
str1 = list(input())
str2 = list(input())
count = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            count[i][j] = count[i-1][j-1] + 1
        else:
            count[i][j] = max(count[i-1][j], count[i][j-1])
print(count[len(str1)][len(str2)])
