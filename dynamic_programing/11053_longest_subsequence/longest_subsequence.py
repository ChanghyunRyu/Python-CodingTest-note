n = int(input())
A = list(map(int, input().split()))


def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid
    return end


dp = [0]*n
B = [A[0]]
for i in range(1, n):
    if A[i] > B[len(B)-1]:
        B.append(A[i])
        dp[i] = len(B)
    else:
        pos = binary_search(A[i], B)
        dp[i] = pos
        if A[i] < B[pos]:
            B[pos] = A[i]
print(len(B))
