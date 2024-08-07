def solution(cloths):
    closet = {}
    for cloth in cloths:
        name, tag = cloth[0], cloth[1]
        if tag not in closet:
            closet[tag] = 1
        else:
            closet[tag] += 1

    answer = 1
    for tag in closet:
        answer *= closet[tag]+1
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
