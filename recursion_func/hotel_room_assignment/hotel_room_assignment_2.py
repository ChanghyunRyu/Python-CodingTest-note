import sys
sys.setrecursionlimit(3000)


def solution(k, room_number):
    answer = []
    room = dict()
    for r in room_number:
        answer.append(assign_room(r, room))
    return answer


def assign_room(number, rooms):
    if number not in rooms:
        rooms[number] = number+1
        return number
    empty = assign_room(rooms[number], rooms)
    rooms[number] = empty+1
    return empty


print(solution(10, [1, 3, 4, 1, 3, 1]))