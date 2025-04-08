n = int(input())
candies = []
for _ in range(n):
    candies.append(list(input()))


def search_candy():
    result = 1
    for i in range(n):
        count = 1
        check = candies[i][0]
        for j in range(1, n):
            if check == candies[i][j]:
                count += 1
                result = max(result, count)
            else:
                count = 1
                check = candies[i][j]

        count = 1
        check = candies[0][i]
        for j in range(1, n):
            if check == candies[j][i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
                check = candies[j][i]
    return result


answer = 0
for cx in range(n):
    for cy in range(n-1):
        if cx+1 < n:
            candies[cx][cy], candies[cx + 1][cy] = candies[cx + 1][cy], candies[cx][cy]
            answer = max(answer, search_candy())
            candies[cx][cy], candies[cx + 1][cy] = candies[cx + 1][cy], candies[cx][cy]

        if cy+1 < n:
            candies[cx][cy], candies[cx][cy + 1] = candies[cx][cy + 1], candies[cx][cy]
            answer = max(answer, search_candy())
            candies[cx][cy], candies[cx][cy + 1] = candies[cx][cy + 1], candies[cx][cy]

print(answer)
