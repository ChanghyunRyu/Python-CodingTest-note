t = int(input())
n_list = []
k_list = []
for i in range(t):
    k_list.append(int(input()))
    n_list.append(int(input()))
# k층 n호
apart = [[-1 for i in range(15)] for i in range(15)]
for i in range(t):
    k = k_list[i]
    n = n_list[i]
    for floor in range(k+1):
        for number in range(n):
            if apart[floor][number] == -1:
                if floor == 0:
                    apart[floor][number] = number+1
                else:
                    people = 0
                    for j in range(number+1):
                        people += apart[floor-1][j]
                    apart[floor][number] = people
    print(apart[k][n-1])
