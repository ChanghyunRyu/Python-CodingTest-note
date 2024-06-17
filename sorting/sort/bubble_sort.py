sample = [3, 0, 1, 8, 7, 2]


def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


print(bubble_sort(sample))
