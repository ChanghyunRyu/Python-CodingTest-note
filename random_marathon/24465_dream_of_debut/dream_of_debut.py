def classification_birthday(birth):
    check = 100*birth[0]+birth[1]
    if 120 <= check <= 218:
        return 0
    elif 219 <= check <= 320:
        return 1
    elif 321 <= check <= 419:
        return 2
    elif 420 <= check <= 520:
        return 3
    elif 521 <= check <= 621:
        return 4
    elif 622 <= check <= 722:
        return 5
    elif 723 <= check <= 822:
        return 6
    elif 821 <= check <= 922:
        return 7
    elif 923 <= check <= 1022:
        return 8
    elif 1023 <= check <= 1122:
        return 9
    elif 1123 <= check <= 1221:
        return 10
    else:
        return 11


constellation = [False]*12
for _ in range(7):
    birthday = list(map(int, input().split()))
    stella = classification_birthday(birthday)
    constellation[stella] = True

n = int(input())
answer = []
for _ in range(n):
    birthday = list(map(int, input().split()))
    stella = classification_birthday(birthday)
    if constellation[stella]:
        continue
    answer.append(birthday)

answer.sort()
if len(answer) == 0:
    print('ALL FAILED')
else:
    for month, day in answer:
        print('{} {}'.format(month, day))
