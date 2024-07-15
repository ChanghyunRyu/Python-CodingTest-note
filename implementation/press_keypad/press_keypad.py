def solution(numbers, hand):
    left_now = '*'
    right_now = '#'
    points = {
        '1': (0, 0),
        '2': (1, 0),
        '3': (2, 0),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '7': (0, 2),
        '8': (1, 2),
        '9': (2, 2),
        '*': (0, 3),
        '0': (1, 3),
        '#': (2, 3)
    }
    answer = []
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer.append('L')
            left_now = str(number)
        elif number == 3 or number == 6 or number == 9:
            answer.append('R')
            right_now = str(number)
        else:
            number_point = points[str(number)]
            left_point = points[left_now]
            right_point = points[right_now]

            left_dis = abs(number_point[0]-left_point[0])+abs(number_point[1]-left_point[1])
            right_dis = abs(number_point[0]-right_point[0])+abs(number_point[1]-right_point[1])
            if left_dis < right_dis:
                answer.append('L')
                left_now = str(number)
            elif left_dis > right_dis:
                answer.append('R')
                right_now = str(number)
            else:
                if hand == 'right':
                    answer.append('R')
                    right_now = str(number)
                else:
                    answer.append('L')
                    left_now = str(number)
    answer = ''.join(answer)
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))

