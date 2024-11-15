def solution(menu, order, k):
    prefix_sum = [0]*(100*(len(order)+1))
    time = 0
    for i in range(len(order)):
        start = i*k
        end = max(start, time)+menu[order[i]]
        prefix_sum[start] += 1
        prefix_sum[end] -= 1
        time = end
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] += prefix_sum[i-1]
    answer = max(prefix_sum)
    return answer

