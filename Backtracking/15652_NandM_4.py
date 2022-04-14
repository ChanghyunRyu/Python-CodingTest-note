n, m = map(int, input().split())


def NandM(number: int, num_list: list):
    if len(num_list) > 0 and number < num_list[len(num_list)-1]:
        return
    else:
        num_list.append(number)
        if len(num_list) == m:
            for num in num_list:
                print(num, end=' ')
            print()
            return
        else:
            for i in range(n):
                NandM(i+1, list(num_list))


for i in range(n):
    NandM(i+1, [])
