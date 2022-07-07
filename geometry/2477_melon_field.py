# 1: 오른쪽, 2: 왼쪽, 3: 아래, 4: 위
# 첫번째 실패: 작은 사각형을 나타내는 x, y 축이 떨어져서 나올 수 있을 거라는 생각을 하지 못 했다.
# 해결: x, y에서 각각 큰 변을 맞는 부분에서 양 옆의 변이 작은 사각형 이외의 변이라는 것을 통해 해결
k = int(input())
length_list = []
for i in range(6):
    direction, length = map(int, input().split())
    length_list.append(length)
max_x_idx = 0
max_y_idx = 1
for i in range(6):
    if i % 2 == 0 and length_list[max_x_idx] < length_list[i]:
        max_x_idx = i
    elif i % 2 == 1 and length_list[max_y_idx] < length_list[i]:
        max_y_idx = i
max_x, max_y = length_list[max_x_idx], length_list[max_y_idx]
all_set = {0, 1, 2, 3, 4, 5}
index_set = {(max_x_idx + 1) % 6, (max_x_idx - 1) % 6, (max_y_idx - 1) % 6, (max_y_idx + 1) % 6}

small_list = list(all_set-index_set)
area = (max_x*max_y) - (length_list[small_list[0]]*length_list[small_list[1]])
print(k*area)
