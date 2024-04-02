## 부품 찾기

-------

시간 제한: 1초, 메모리 제한: 128MB

### 입력

- 첫째 줄에 정수 N이 주어진다.
- 둘째 줄에 공백으로 구분하여 N개의 정수가 주어진다. 
- 셋째 줄에는 정수 M이 주어진다.
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.

### 출력

- 첫째 줄에 공백으로 구분하여 가 부품이 존재하면 yes를, 없으면 no를 출력한다.

~~~
n = int(input())
arr = list(map(int, input().split()))

m = int(input())
part = list(map(int, input().split()))
arr.sort()


def binary_search(target, arr, start, end):
    if end < start:
        return None
    mid = (start+end)//2
    if arr[mid] < target:
        return binary_search(target, arr, mid+1, end)
    elif arr[mid] == target:
        return mid
    else:
        return binary_search(target, arr, start, mid-1)


for p in part:
    result = binary_search(p, arr, 0, len(arr)-1)
    if result is None:
        print('no', end=' ')
    else:
        print('yes', end= ' ')


~~~
