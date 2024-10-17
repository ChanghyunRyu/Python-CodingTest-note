def solution(clothes):
    closet = {}
    for name, cloth_type in clothes:
        if cloth_type in closet:
            closet[cloth_type] += 1
        else:
            closet[cloth_type] = 1
    answer = 1
    for key in closet:
        answer *= closet[key]+1
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
