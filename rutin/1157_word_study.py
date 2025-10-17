word = input()
d = {}
max_num = 0
result = ''
for w in word:
    w = w.upper()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
    if d[w] > max_num:
        max_num = d[w]
        result = w
    elif d[w] == max_num and result != '?' and result != w:
        result = '?'
print(result)
