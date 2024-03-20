array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


for i in range(len(array)):
    min_idx = i
    for k in range(i+1, len(array)):
        if array[min_idx] > array[k]:
            min_idx = k
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)
