## 2447번 별 찍기 - 10

---

시간 제한: 1초, 메모리 제한: 256MB

재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

~~~
***
* *
***
~~~

N이 3보다 클 경우, 
크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

### 입력

- 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 
- 즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.

### 출력

- 첫째 줄부터 N번째 줄까지 별을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/06/12
- [ ] 2회
- [ ] 3회

스스로 생각해낸 것은 좋았으나 예전 풀이에 비해 소요 시간이 늘어났다.
다음에는 조금 더 소요 시간을 단축시키는 방향으로 풀이를 해봐야 할 것.

~~~
n = int(input())


def create_star(num, is_blank):
    if is_blank:
        return [[0]*num for _ in range(num)]
    if num == 3:
        return [[1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]]
    temp = [[0]*num for _ in range(num)]
    for i in range(3):
        for j in range(3):
            start_x = i*(num//3)
            start_y = j*(num//3)
            if i == 1 and j == 1:
                star_arr = create_star(num//3, True)
            else:
                star_arr = create_star(num//3, False)
            for x in range(len(star_arr)):
                for y in range(len(star_arr)):
                    nx = start_x+x
                    ny = start_y+y
                    temp[nx][ny] = star_arr[x][y]
    return temp


arr = create_star(n, False)
for line in arr:
    for num in line:
        if num == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

~~~