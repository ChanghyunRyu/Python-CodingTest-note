def solution(strings, n):
    answer = sorted(strings, key=lambda k: (k[n], k))
    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
