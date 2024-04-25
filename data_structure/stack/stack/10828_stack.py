import sys
k = int(input())

stack = []
for _ in range(k):
    string = list(sys.stdin.readline().split())
    if string[0] == 'push':
        stack.append(int(string[1]))
    elif string[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif string[0] == 'size':
        print(len(stack))
    elif string[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
