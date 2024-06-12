def solution(brown, yellow):
    answer = []
    sum_width_length = (brown+4)//2
    length = 3
    width = sum_width_length-length
    while length <= width:
        if yellow == (width*length)-brown:
            answer.append(width)
            answer.append(length)
            break
        length += 1
        width = sum_width_length-length
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
