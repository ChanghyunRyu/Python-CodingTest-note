from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while people:
        min_person = people.popleft()
        while people and people[-1]+min_person > limit:
            people.pop()
            answer += 1
        if people:
            people.pop()
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([40, 45, 50, 50, 55, 60], 150))
print(solution([50, 50, 50, 50], 200))
print(solution([20, 60, 70, 80, 30], 100))
