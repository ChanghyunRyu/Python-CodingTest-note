# 문자열 a->1로 변환하는 부분에서 착각했음. 다른 언어처럼 a에 +1을 단순히 해준다고 b가 되지않음.
input_data = input()
row = int(input_data[1])
# ord(): 문자열->유니코드정수, chr(): 유니코드->문자열 정수
col = int(ord(input_data[0])-ord('a'))+1

# 처음에 해당 방법을 떠올렸으나 수작업이 많을 것 같아 배제 But 행렬로 만들어 각 작업을 지정해주는 것은 괜찮은 코딩으로 보임.
steps = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
count = 0
for step in steps:
    row_pre = row + step[0]
    col_pre = col + step[1]
    if 8 >= row_pre >= 1 and 8 >= col_pre >= 1:
        count += 1
print(count)