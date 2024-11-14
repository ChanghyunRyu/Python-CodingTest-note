## 2117. [모의 SW 역량테스트] 홈 방범 서비스

---

[문제] https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&

---

### 풀이
### Problem Solved Check
- [x] 1회 24/11/14
- [ ] 2회
- [ ] 3회

손해만 안 나면 되기에 이득이 0이여도 체크를 해줘야 한다. 그 부분 실수해서 한 번 오답
~~~
def get_home(x, y):
    home = [0]*(2*N)
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                dist = abs(x-i)+abs(y-j)+1
                home[dist] += 1
    return home


def calc_cost(k):
    return k**2+(k-1)**2


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    city = []
    for _ in range(N):
        city.append(list(map(int, input().split())))
        
    answer = 0
    for i in range(N):
        for j in range(N):
            now_home = get_home(i, j)
            homes = 0
            for d in range(1, 2*N):
                cost = calc_cost(d)
                homes += now_home[d]
                if homes*M - cost >= 0:
                    answer = max(answer, homes)
    print('#{} {}'.format(test_case, answer))       

~~~