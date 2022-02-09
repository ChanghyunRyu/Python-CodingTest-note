n = int(input())
# n시 59분 59초 이기때문 n+1을 하는 것을 빼먹은 적이 있음.
n_seconds = (n+1)*60*60
count = 0
for i in range(n_seconds):
    hour = i//3600
    min = (i-(hour*3600))//60
    second = ((i-(hour*3600))-(min*60))
    if hour == 3 or hour % 10 == 3 or min == 3 or min//10 == 3 or min % 10 == 3 or second == 3 or second//10 == 3 or second % 10 == 3:
        count += 1
print(count)
