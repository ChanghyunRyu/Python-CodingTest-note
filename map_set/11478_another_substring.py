string = input()
substring = set()
for i in range(len(string)):
    for j in range(len(string)-i):
        sub = string[i:i+j+1]
        substring.add(sub)
print(len(substring))
