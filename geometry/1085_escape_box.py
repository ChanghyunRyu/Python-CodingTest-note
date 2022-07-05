x, y, w, h = map(int, input().split())
length_array = []
length_array.append(abs(x-w))
length_array.append(abs(y-h))
length_array.append(x)
length_array.append(y)
length_array.sort()
print(length_array[0])
