sticks = list(map(int, input().split()))
sticks.sort()

print(sticks[0]+sticks[1]+min(sticks[2], sticks[0]+sticks[1]-1))
