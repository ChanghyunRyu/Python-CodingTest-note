## 실습용 로봇

---

[출처] https://school.programmers.co.kr/learn/courses/15009/lessons/121687

컴퓨터공학과에서는 실습용 로봇을 이용해서 로봇 프로그래밍을 학습합니다. 실습용 로봇은 입력된 명령에 따라 x좌표와 y좌표로 표현되는 2차원 좌표 평면 위를 이동합니다. 하나의 명령은 하나의 문자로 주어지며 각 명령어에 따라 로봇이 수행하는 일은 다음과 같이 네 종류입니다.

- 'R': 로봇이 오른쪽으로 90도 회전합니다.
- 'L': 로봇이 왼쪽으로 90도 회전합니다.
- 'G': 로봇이 한 칸 전진합니다.
- 'B': 로봇이 한 칸 후진합니다.

명령어는 각각의 명령들이
모인 하나의 문자열로 주어지며, 차례대로 수행됩니다.

로봇에 입력된 명령어를 순서대로 담고 있는 문자열 command가 주어집니다. 로봇이 주어진 명령어들을 순서대로 모두 수행한 뒤 
도착한 최종 위치의 좌푯값 x, y를 순서대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- 1 ≤ commad의 길이 ≤ 1,000,000
- command는 'R', 'L', 'G', 'B'으로 구성된 문자열입니다.
- command에 들어있는 문자 하나하나가 각 명령을 나타내며, 문자열에 먼저 등장하는 명령을 먼저 수행해야 합니다.

---
### Problem Solved Check
- [x] 1회 24/09/23
- [ ] 2회
- [ ] 3회
~~~
def solution(command):
    answer = [0, 0]
    nxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    idx = 0
    for c in command:
        if c == 'G':
            answer[0] += nxy[idx][0]
            answer[1] += nxy[idx][1]
        elif c == 'B':
            answer[0] -= nxy[idx][0]
            answer[1] -= nxy[idx][1]
        elif c == 'R':
            idx = (idx+1) % 4
        elif c == 'L':
            idx = (idx-1) % 4
    return answer


print(solution("GRGLGRG"))
print(solution("GRGRGRB"))
~~~