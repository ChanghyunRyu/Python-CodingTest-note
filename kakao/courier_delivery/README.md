## 택배 배달과 수거하기

---

[문제] https://school.programmers.co.kr/learn/courses/30/lessons/150369

### Problem Solved
- [x] 1회 24/12/26
- [ ] 2회
- [ ] 3회

### 첫 풀이

간단하게 가야할 거리 측정, 측정한 거리까지 배달할 수 있는 만큼 배달하고 수거할 수 있는 만큼 수거하기.  
정답은 맞았으나 시간 초과로 실패.

둘 모두 꽉 차면 탈출하도록 식을 짰는데, 아무래도 최상의 경우에는 O(n) 처럼 작동할 거라 생각했는데 생각해보니 
한 쪽이 0으로 이루어진 배열이면 사실상 O(n^2)의 시간복잡도를 가진다.

~~~
def solution(cap, n, deliveries, pickups):
    answer = 0
    start = n-1
    while start >= 0:
        # 가야할 거리 측정
        while start >= 0:
            if deliveries[start] != 0 or pickups[start] != 0:
                break
            start -= 1
        answer += 2*(start+1)

        dt = 0
        pt = 0
        flag = True
        for i in range(start, -1, -1):
            if dt+deliveries[i] < cap:
                dt += deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= cap - dt
                dt = cap

            if pt+pickups[i] < cap:
                pt += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= cap-pt
                pt = cap
            if flag and deliveries[i] == 0 and pickups[i] == 0:
                start = i-1
            else:
                flag = False
            if pt == cap and dt == cap:
                break
    return answer
~~~

### 스택을 이용한 풀이

가야할 거리 측정, 측정한 거리까지 배달할 수 있는 만큼 배달하고 수거할 수 있는 만큼 수거하는 건 동일.  
1. 배달, 수거할 게 없는 집의 경우 pop해서 모두 제거해준다.
2. 배달, 수거해야할 집들 중 가장 먼 거리를 측정 x 2 를 해서 정답에 더해준다.
3. 배달, 수거 배열에서 하나씩 pop 하면서 배달, 수거가 가능한 지 체크해준다.
    1. 수거 가능한 갯수를 초과한 경우, 더 이상 수거하지 않고 초과된 수거량만큼 배열에 다시 더해준다.

뒤에서부터 해결하는 방법이므로 스택을 사용하면 된다는 생각을 바로하지 못 한게 아쉬운 문제. 

~~~
def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and pickups and deliveries[-1] == 0 and pickups[-1] == 0:
            deliveries.pop()
            pickups.pop()
        distance = max(len(deliveries), len(pickups))
        answer += 2*distance

        dt = 0
        while deliveries:
            dt += deliveries.pop()
            if dt > cap:
                deliveries.append(dt-cap)
                break

        pt = 0
        while pickups:
            pt += pickups.pop()
            if pt > cap:
                pickups.append(pt-cap)
                break
    return answer
~~~