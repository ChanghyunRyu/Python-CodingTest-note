## 운영체제

---

[출처] https://school.programmers.co.kr/learn/courses/15008/lessons/121686

개발자 준모는 운영체제를 만들었습니다. 준모가 만든 운영체제는 프로그램의 우선순위와 호출된 시각에 따라 실행 순서를 결정합니다. 
모든 프로그램에는 1부터 10까지의 점수가 매겨져 있으며, 이 점수가 낮을수록 우선순위가 높은 프로그램입니다. 
각 프로그램들은 실행 시간이 정해져 있으며 프로그램이 호출되면 대기상태에 있다가 자신의 순서가 되면 실행 시간 동안 실행된 뒤 종료됩니다.

준모가 만든 운영체제는 호출된 프로그램들 중 우선순위가 가장 높은 프로그램을 먼저 실행합니다. 
호출된 각 프로그램은 자신보다 우선순위가 높은 호출된 프로그램이 모두 종료된 후에 실행됩니다. 
단, 실행 중인 프로그램보다 우선순위가 높은 프로그램이 호출되어도 실행 중이던 프로그램은 중단되지 않고 
종료될 때까지 계속 실행됩니다. 또한, 우선순위가 같은 프로그램들 중에서는 먼저 호출된 프로그램이 먼저 실행됩니다.

프로그램들의 정보를 나타내는 2차원 정수 배열 program이 주어질 때, 모든 프로그램들이 종료되는 시각과 프로그램의 점수마다 대기시간의 합을 정수 배열에 담아 
return 하는 solution 함수를 완성하세요. return 해야 하는 answer 배열은 길이가 11인 정수 배열입니다. 
answer[0]은 모든 프로그램들이 종료되는 시각을 의미하며, answer[i](1 ≤ i ≤ 10)는 
프로그램의 점수가 i인 프로그램들의 대기시간의 합을 의미합니다.

### 제한 사항

- 1 ≤ program의 길이 ≤ 100,000
- program[i]은 i+1번 프로그램의 정보를 의미하며, [a, b, c]의 형태로 주어집니다.
  - a는 프로그램의 점수를 의미하며, 1 ≤ a ≤ 10 을 만족합니다.
  - b는 프로그램이 호출된 시각을 의미하며, 0 ≤ b ≤ 10,000,000을 만족합니다.
  - c는 프로그램의 실행 시간을 의미하며, 1 ≤ c ≤ 1,000을 만족합니다.
  - a, b쌍이 중복되는 프로그램은 입력으로 주어지지 않습니다. 즉, 호출된 시각이 같으면서 점수도 같은 프로그램은 없습니다.

---
### Problem Solved Check
- [x] 1회 24/10/01 
- [x] 2회 24/11/15
- [ ] 3회
~~~
import heapq


def solution(program):
    answer = [0]*11
    q = []
    program = sorted(program, key=lambda x: (x[1], x[0]), reverse=True)
    now = 0
    while q or program:
        if not q:
            heapq.heappush(q, program.pop())
        score, start, time = heapq.heappop(q)
        if now > start:
            answer[score] += now-start
        now = max(now, start) + time
        while program:
            if program[-1][1] > now:
                break
            heapq.heappush(q, program.pop())
    answer[0] = now
    return answer
    
~~~
~~~
import heapq


def solution(program):
    answer = [0]*11
    program.sort(key=lambda x: x[1], reverse=True)
    time = 0
    process = []
    while process or program:
        while process:
            now = heapq.heappop(process)
            answer[now[0]] += time-now[1]
            time += now[2]
            while program and program[-1][1] <= time:
                heapq.heappush(process, program.pop())
        if program:
            temp = program.pop()
            heapq.heappush(process, temp)
            time = temp[1]
            while program and program[-1][1] <= time:
                heapq.heappush(process, program.pop())
    answer[0] = time
    return answer

~~~