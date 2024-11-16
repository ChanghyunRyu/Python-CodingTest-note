def solution(nums):
    answer = 0
    ponkemon = {}
    for num in nums:
        if num in ponkemon:
            ponkemon[num] += 1
        else:
            ponkemon[num] = 1
    answer = min(len(nums)//2, len(ponkemon))
    return answer

