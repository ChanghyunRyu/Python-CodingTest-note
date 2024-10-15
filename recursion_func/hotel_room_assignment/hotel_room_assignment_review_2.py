import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    answer = []
    hotel = {}
    for number in room_number:
        answer.append(assign_room(hotel, number))
    return answer


def assign_room(hotel, room_number):
    if room_number not in hotel:
        hotel[room_number] = room_number+1
        return room_number
    else:
        assign_number = assign_room(hotel, hotel[room_number])
        hotel[room_number] = assign_number
        return assign_number


print(solution(10, [1, 3, 4, 1, 3, 1]))
