def solution(s):
    answer = {}
    data = s[2:-2].split('},{')

    data.sort(key=len)
    for d in data:
        nums = d.split(',')
        for num in nums:
            if num not in answer:
                answer[int(num)] = True
    return list(answer)


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
