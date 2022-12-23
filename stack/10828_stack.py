import sys

stack = []
n = int(input())
for i in range(n):
    input_string = sys.stdin.readline()
    split_string = input_string.split()
    if split_string[0] == 'push':
        stack.append(int(split_string[1]))
    elif split_string[0] == 'pop':
        if len(stack) != 0:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
        else:
            print(-1)
    elif split_string[0] == 'size':
        print(len(stack))
    elif split_string[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif split_string[0] == 'top':
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
