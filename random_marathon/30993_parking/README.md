## 30993번 자동차 주차

---

시간 제한: 1초, 메모리 제한: 1024MB

같은 차종의 빨간색 자동차 A대, 초록색 자동차 B대, 파란색 자동차 C대를 N칸의 주차장에 1대씩 주차하려고 한다.

모든 자동차를 한 칸에 한 대씩 주차할 수 있는 경우의 수를 구하라.

### 입력

- 첫 번째 줄에 양의 정수 N, A, B, C가 공백으로 주어진다.
- A+B+C = N <= 15

### 출력

- 첫 번째 줄에 정답을 출력한다. 

---

조합을 통해서 구하는 문제. 
~~~
n, a, b, c = map(int, input().split())


def get_combination_number(N, C):
    temp = 1
    temp2 = 1
    for i in range(C):
        temp *= i+1
        temp2 *= N-i
    return temp2//temp


result = 1
result *= get_combination_number(n, a)
n -= a
result *= get_combination_number(n, b)
print(result)

~~~
