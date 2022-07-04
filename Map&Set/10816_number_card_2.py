# 카드의 숫자를 세게한다는 점, 계수정렬을 사용
# => 이 경우, 시간보다는 메모리에서 허용범위를 넘어갈 가능성이 있으니 체크
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

card_numbering = [0 for i in range(20000001)]
for card in cards:
    card_numbering[card + 10000000] += 1
for check in checks:
    print(card_numbering[check+10000000], end=' ')
