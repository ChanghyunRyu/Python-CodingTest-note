# 공포도가 k인 모험가는 k명 이상인 그룹에 참여해야 여행을 떠날 수 있다.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하여라
# 2 3 1 2 2 -> 1 2 2 2 3
n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()
i = count = 0
for adventurer in adventurers:
    i += 1
    if i == adventurer:
        count += 1
        i = 0

print(count)
