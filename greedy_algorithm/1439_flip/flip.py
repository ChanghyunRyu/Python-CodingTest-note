txt = list(map(int, input()))
result = [0]*2
for i in range(1, len(txt)):
    if txt[i-1] != txt[i]:
        result[txt[i-1]] += 1
    if i == len(txt)-1:
        result[txt[i]] += 1
print(min(result))
