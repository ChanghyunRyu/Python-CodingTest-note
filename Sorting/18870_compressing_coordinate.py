# 숫자의 범위가 너무 크다(-10억 ~ 10억) = 계수 정렬 x
# list->set 변형하는 경우, 기존에 가지고 있던 순서가 없어진다. 정렬->변환이 아니라 변환->정렬을 해야한다.
n = int(input())
numbers = list(map(int, input().split()))
number_set = set(numbers)
number_set = sorted(number_set)
num_dict = dict()
count = 0
for num in number_set:
    num_dict[num] = count
    count += 1
for number in numbers:
    print(num_dict[number], end=' ')
