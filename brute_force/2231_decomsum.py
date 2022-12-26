# 처음 설계할 때, 생성자가 없는 경우 0을 출력하는 부분을 빼먹음(꼼꼼하게 보자!)
n = int(input())
for num in range(1, n+1):
    decomposition = num
    num_str = str(num)
    for pos in num_str:
        decomposition += int(pos)
    if decomposition == n:
        print(num)
        break
    if num == n:
        print(0)
