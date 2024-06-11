def solution(k, room_number):
    answer = []
    for r in room_number:
        assign_room(r, answer)
    return answer


def assign_room(number, a):
    if number in a:
        assign_room(number+1, a)
    else:
        a.append(number)


print(solution(10, [1, 3, 4, 1, 3, 1]))
