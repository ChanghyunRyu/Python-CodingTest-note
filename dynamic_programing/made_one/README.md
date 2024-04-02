## 1로 만들기

---

시간 제한: 1초, 메모리 제한: 128MB

정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

- X가 5로 나누어떨어지면, 5로 나눈다.
- X가 3으로 나누어떨어지면, 3으로 나눈다.
- X가 2로 나누어떨어지면, 2로 나눈다.
- X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

### 입력

- 첫째 줄에 정수 X가 주어진다. (1 ≤ X ≤ 30,000)

### 출력

- 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

---

~~~
x = int(input())

arr = [0]*30001
arr[1], arr[2] = 1, 1

for i in range(3, x):
    result = arr[i-1]
    if i % 5 == 0:
        result = min(result, arr[i//5])
    elif i % 3 == 0:
        result = min(result, arr[i//3])
    elif i % 2 == 0:
        result = min(result, arr[i//2])
    arr[i] = result + 1

print(arr[x-1])
~~~
