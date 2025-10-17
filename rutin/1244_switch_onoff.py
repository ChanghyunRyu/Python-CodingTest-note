sn = int(input())
switch = list(map(int, input().split()))
n = int(input())


def swap_switch(s):
    if s == 1:
        return 0
    else:
        return 1


def change_switch(gender, num):
    if gender == 1:
        count = 1
        while count*num <= sn:
            switch[count*num-1] = swap_switch(switch[count*num-1])
            count += 1
    else:
        start = num-1
        switch[start] = swap_switch(switch[start])
        count = 1
        while start+count < sn and start-count >= 0:
            if switch[start+count] == switch[start-count]:
                switch[start + count] = swap_switch(switch[start+count])
                switch[start - count] = swap_switch(switch[start-count])
                count += 1
            else:
                break


for _ in range(n):
    g, number = map(int, input().split())
    change_switch(g, number)

start = 0
for i in range(len(switch)):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()
