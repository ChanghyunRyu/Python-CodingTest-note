def cantor(num, is_blank):
    if is_blank:
        return ' '*(3**num)
    if num == 0:
        return '-'
    return ''.join([cantor(num-1, False), cantor(num-1, True), cantor(num-1, False)])


while True:
    try:
        n = int(input())
        print(cantor(n, False))
    except:
        break
