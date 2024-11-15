import heapq


def solution(program):
    answer = [0]*11
    program.sort(key=lambda x: x[1], reverse=True)
    time = 0
    process = []
    while process or program:
        while process:
            print('{}')
            now = heapq.heappop(process)
            answer[now[0]] += time-now[1]
            time += now[2]
            while program and program[-1][1] <= time:
                heapq.heappush(process, program.pop())
        if program:
            temp = program.pop()
            heapq.heappush(process, temp)
            time = temp[1]
            while program and program[-1][1] <= time:
                heapq.heappush(process, program.pop())
    return answer


print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
