# nC3 = n(n-1)(n-2)/6 = O(n^3)
# 처음 실수: 인덱스 설정할 때, i1+1, i2+1을 안 해줘서 처음에는 같은 수끼리 더하는 케이스들이 생김
n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

max_num = 0
for i1 in range(len(cards)):
    num1 = cards[i1]
    for i2 in range(i1+1, len(cards)):
        num2 = cards[i2]
        for i3 in range(i2+1, len(cards)):
            num3 = cards[i3]
            num_sum = num1+num2+num3
            if num_sum > m:
                continue
            else:
                if num_sum > max_num:
                    max_num = num_sum
print(max_num)
