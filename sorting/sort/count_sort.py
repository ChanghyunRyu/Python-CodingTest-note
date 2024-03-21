arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

arr2 = [0]*(max(arr)+1)
for num in arr:
    arr2[num] += 1

for i in range(len(arr2)):
    for _ in range(arr2[i]):
        print(i, end=' ')
