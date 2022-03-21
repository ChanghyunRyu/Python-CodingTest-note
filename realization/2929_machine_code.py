commend = input()
num = -3
count = 0
# 간단한 코딩이지만 문제 해석을 잘못 했음.
# 1. 시작 순서를 4의 배수로 맞추기만하면 되기때문에 마지막은 카운팅 x
# 2. 패러미터가 4개 이상일 수 있다.
for character in commend:
    if character.isupper():
        num += 3 - (count % 4)
        count = 0
    else:
        count += 1
print(num)
