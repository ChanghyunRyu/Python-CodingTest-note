# 오직 증가만 하는 수열, 증가하다가 감소하는 함수, 오직 감소만 하는 함수
# 증가하는 수열 + 감소하는 수열 두가지만 저장하면 된다.
# 각 인덱스에서 앞쪽으로 증가하는 함수 + 뒤쪽으로 감소하는 최대 길이를 더하면 해당 인덱스에서 방향을 바꾸는 가장 긴 수열의 길이가 나온다.
# 그 중 최대값이 정답
n = int(input())
sequence = list(map(int, input().split()))
counts = [1] * len(sequence)
reverse_counts = [1] * len(sequence)
for i in range(1, len(sequence)):
    temp = 1
    reverse_temp = 1
    for j in range(i):
        if sequence[i] > sequence[i-j-1] and temp < counts[i-j-1] + 1:
            temp = counts[i-j-1] + 1
        if sequence[n-i-1] > sequence[n-i+j] and reverse_temp < reverse_counts[n-i+j] + 1:
            reverse_temp = reverse_counts[n-i+j] + 1
    reverse_counts[n-i-1] = reverse_temp
    counts[i] = temp
for i in range(len(counts)):
    counts[i] = counts[i] + reverse_counts[i] - 1
print(max(counts))
