def solution(answers):
    answer = []
    test_taker = [[1, 2, 3, 4, 5],
                  [2, 1, 2, 3, 2, 4, 2, 5],
                  [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    collect = [0]*3
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == test_taker[j][i%len(test_taker[j])]:
                collect[j] += 1
    result = max(collect)
    for i in range(3):
        if collect[i] == result:
            answer.append(i+1)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
