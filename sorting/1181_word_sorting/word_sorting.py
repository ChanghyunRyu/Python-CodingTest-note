import sys

# 입력 배열
n = int(input())
arr = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    length = len(word)
    value = (length, word)
    # 중복 제거
    if value not in arr:
        arr.append(value)

arr.sort()
for w in arr:
    print(w[1])
