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
