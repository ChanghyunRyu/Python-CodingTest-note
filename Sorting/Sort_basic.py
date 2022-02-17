data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
        if data[j] < data[min_index]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]
print(data)

# 삽입 정렬
# 시간 복잡도는 선택정렬과 같은 O(n^2)이나 이미 정렬되어 있는 데이터일수록 시간 복잡도가 낮아진다.
# 최고의 경우, O(n) 시간복잡도를 가짐.
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break
print(data)

# 퀵정렬
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(data, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)


quick_sort(data, 0, len(data)-1)
print(data)
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 새로 배열을 만들어서 해결하는 방법
# 평균 시간복잡도 O(n*log(n))
def quick_sort_python(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    tail = data[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)


print(quick_sort_python(data))
