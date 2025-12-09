import sys


n = int(input())
channel = []
for _ in range(n):
    channel.append(sys.stdin.readline().strip())

result = []
# find & Change KBS1
for i in range(len(channel)):
    if channel[i] == "KBS1":
        result.append("1"*i)
        result.append("4"*i)
        del channel[i]
        break

# find & Change KBS2
for i in range(len(channel)):
    if channel[i] == "KBS2":
        result.append("1"*(i+1))
        result.append("4"*i)
        del channel[i]
        break

print(''.join(result))
