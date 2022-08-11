# 해설: 누적합에서 특정 구간의 합을 구하는 방법은 (i번째 누적합 - j번째 누적합) 통해 계산된다.
# 즉, 숫자 m에 대한 i번째 누적합의 나머지와 j번재 누적합의 나머지가 같을 경우(= j~i번 까지의 합)는 m으로 나누어 떨어지는 수인 것이다.
# 따라서 나머지가 같은 수의 개수를 기록한 후, 나머지가 같은 누적합 중 2개를 뽑는 경우를 더해주면 된다.
# 여기서 나머지가 0인 누적합들은 그 자체적으로 정답이 되기때문에 처음에 더해준다.

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
result = 0
remainders = [0]*m
for num in nums:
    result += num
    remainders[result % m] += 1
answer = remainders[0]
for remainder in remainders:
    answer += (remainder*(remainder-1))//2
print(answer)
