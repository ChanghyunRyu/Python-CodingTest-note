# 파이썬의 sorted 함수는 안정 정렬인가? True
# 안정 정렬(stable sort): 값이 같은 원소의 전후 관계가 바뀌지 않는 정렬 알고리즘
n = int(input())
peoples = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    peoples.append((age, name))

peoples = sorted(peoples, key= lambda people: people[0])
for people in peoples:
    print('{} {}'.format(people[0], people[1]))
