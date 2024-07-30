import sys
sys.setrecursionlimit(100000)
record = {}


def solution(k, room_number):
    answer = []
    for number in room_number:
        answer.append(assign_room(number))
    return answer


def assign_room(room_number):
    if room_number not in record:
        record[room_number] = room_number+1
        assign_number = room_number
    else:
        assign_number = assign_room(record[room_number])
        record[room_number] = assign_number+1
    return assign_number


print(solution(10, [1, 3, 4, 1, 3, 1]))
