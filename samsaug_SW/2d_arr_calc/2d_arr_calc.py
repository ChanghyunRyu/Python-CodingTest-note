r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))


def calc_arr(array):
    max_len = 0
    if len(array) >= len(array[0]):
        result = []
        for i in range(len(array)):
            count_number = {}
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    continue
                if array[i][j] in count_number:
                    count_number[array[i][j]] += 1
                else:
                    count_number[array[i][j]] = 1
            temp = []
            for number in count_number:
                temp.append([number, count_number[number]])
            temp.sort(key=lambda x: (x[1], x[0]))
            line = []
            for t in temp:
                line += t
            max_len = max(max_len, len(line))
            result.append(line)
        for i in range(len(result)):
            for _ in range(max_len-len(result[i])):
                result[i].append(0)
    else:
        data = []
        for j in range(len(array[0])):
            count_number = {}
            for i in range(len(array)):
                if array[i][j] == 0:
                    continue
                if array[i][j] in count_number:
                    count_number[array[i][j]] += 1
                else:
                    count_number[array[i][j]] = 1
            temp = []
            for number in count_number:
                temp.append([number, count_number[number]])
            temp.sort(key=lambda x: (x[1], x[0]))
            line = []
            for t in temp:
                line += t
            max_len = max(max_len, len(line))
            data.append(line)
        result = [[0]*(len(array[0])) for _ in range(max_len)]
        for i in range(len(data)):
            for j in range(len(data[i])):
                result[j][i] = data[i][j]
    return result


count = 0
answer = -1
while count <= 100:
    if r-1 < len(arr) and c-1 < len(arr[0]) and arr[r-1][c-1] == k:
        answer = count
        break
    count += 1
    arr = calc_arr(arr)
print(answer)
