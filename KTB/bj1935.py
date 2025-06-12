n = int(input())
expression = input()

dist = {}
for i in range(n):
    dist[chr(65+i)] = int(input())


stack = []
for e in expression:
    if e in dist:
        stack.append(dist[e])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if e == "+":
            result = num1 + num2
        elif e == "-":
            result = num2 - num1
        elif e == "*":
            result = num1 * num2
        elif e == "/":
            result = num2 / num1
        stack.append(result)

print(f"{result:.2f}")
