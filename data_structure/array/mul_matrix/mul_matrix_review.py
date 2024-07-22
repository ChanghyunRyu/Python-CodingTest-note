def solution(matrix1, matrix2):
    answer = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix2[0])):
            mul_temp = 0
            for k in range(len(matrix1[i])):
                mul_temp += matrix1[i][k]*matrix2[k][j]
            temp.append(mul_temp)
        answer.append(temp)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
