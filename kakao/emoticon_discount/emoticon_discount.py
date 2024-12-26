import sys
sys.setrecursionlimit(20000)


def solution(users, emoticons):
    answer = [0, 0]
    dfs(users, emoticons, [], answer)
    return answer


def dfs(users, emoticons, discount, result):
    if len(discount) == len(emoticons):
        subscribe = 0
        total = 0
        for target, price in users:
            p_sum = 0
            for i in range(len(discount)):
                if discount[i] >= target:
                    p_sum += int(emoticons[i] // 100 * (100-discount[i]))
            if p_sum >= price:
                subscribe += 1
                p_sum = 0
            total += p_sum
        if result[0] < subscribe:
            result[0] = subscribe
            result[1] = total
        elif result[0] == subscribe and result[1] < total:
            result[0] = subscribe
            result[1] = total
        return

    for i in range(1, 5):
        temp = list(discount)
        temp.append(10*i)
        dfs(users, emoticons, temp, result)


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
print(solution([[10, 100]], [10, 10, 10, 10, 5000]))
