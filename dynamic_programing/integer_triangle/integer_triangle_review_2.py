def solution(triangles):
    dp = [[0]*(i+1) for i in range(len(triangles))]
    dp[0][0] = triangles[0][0]

    for i in range(1, len(triangles)):
        for j in range(len(triangles[i])):
            temp = []
            if j-1 >= 0:
                temp.append(dp[i-1][j-1])
            if j < len(triangles[i-1]):
                temp.append(dp[i-1][j])
            dp[i][j] = max(temp)+triangles[i][j]
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
