# 하노이는 어째서 재귀일까?
# if - 1) 1-3
# if - 2) 1-2 1-3 2-3
# 하노이를 1 -> 3에 국한되어 만들지 않는다면 어떨까?
# 하노이를 함수(출발, 경유, 도착, 개수)로 만든다면?
# n개의 하노이는 하노이(1,2,3,n) = return 하노이(1,3,2,n-1) + 1->3 + 하노이(2,1,3, n-1)
n = int(input())


def hanoi_count(start, through, end, num, path):
    if num == 1:
        path.append('{} {}'.format(start, end))
    else:
        hanoi_count(start, end, through, num-1, path)
        path.append('{} {}'.format(start, end))
        hanoi_count(through, start, end, num-1, path)


path_list = []
count_num = 0
hanoi_count(1, 2, 3, n, path_list)
print(len(path_list))
for path in path_list:
    print(path)
