n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))


def setting(student):
    return student[1]


data.sort(key=setting)
# data.sort(key=lambda student:student[1]) 즉석 함수 만드는 방법이 더 깔끔함
for student in data:
    print(student[0], end=' ')
