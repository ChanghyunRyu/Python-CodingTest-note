n, k = map(int, input().split())
A = list(map(int, input().split()))
count = []


def mergesort(p, r):
    if p < r:
        q = int((p+r)/2)
        mergesort(p, q)
        mergesort(q+1, r)
        merge(p, q, r)


def merge(p, q, r):
    global A, count
    temp = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if A[i] >= A[j]:
            count.append(A[j])
            temp.append(A[j])
            j += 1
        else:
            count.append(A[i])
            temp.append(A[i])
            i += 1
    while i <= q:
        count.append(A[i])
        temp.append(A[i])
        i += 1
    while j <= r:
        count.append(A[j])
        temp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = temp[t]
        i += 1
        t += 1


mergesort(0, n-1)
if k <= len(count):
    print(count[k-1])
else:
    print(-1)

