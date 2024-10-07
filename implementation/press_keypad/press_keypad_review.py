def solution(numbers, hand):
    points = {
        '*': (0, 0),
        '0': (0, 1),
        '#': (0, 2),
        '1': (3, 0),
        '2': (3, 1),
        '3': (3, 2),
        '4': (2, 0),
        '5': (2, 1),
        '6': (2, 2),
        '7': (1, 0),
        '8': (1, 1),
        '9': (1, 2)
    }

    left_now = '*'
    right_now = '#'
    answer = []
    for num in numbers:
        print('now:{}, left:{}, right:{}'.format(num, left_now, right_now))
        num = str(num)
        temp = return_keypad(num, left_now, right_now, points)
        if temp == 'L':
            answer.append(temp)
            left_now = num
        elif temp == 'R':
            answer.append(temp)
            right_now = num
        else:
            if hand == 'left':
                answer.append('L')
                left_now = num
            else:
                answer.append('R')
                right_now = num
    return ''.join(answer)


def return_keypad(keypad, left, right, points):
    if keypad == '1' or keypad == '4' or keypad == '7':
        return 'L'
    elif keypad == '9' or keypad == '6' or keypad == '3':
        return 'R'

    keypad_point = points[keypad]
    left_point = points[left]
    right_point = points[right]
    left_diff = abs(keypad_point[0]-left_point[0])+abs(keypad_point[1]-left_point[1])
    right_point = abs(keypad_point[0]-right_point[0])+abs(keypad_point[1]-right_point[1])
    if left_diff < right_point:
        return 'L'
    elif left_diff > right_point:
        return 'R'
    else:
        return 'H'


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
