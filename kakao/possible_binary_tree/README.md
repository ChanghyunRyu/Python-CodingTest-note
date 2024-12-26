## 표현 가능한 이진트리

---

[문제] https://school.programmers.co.kr/learn/courses/30/lessons/150367

1. 십진수를 이진수로 변환한다. 

(ex) 95 = 1011111
2. 변환된 이진수의 자릿수를 2^k-1(포화 이진트리 노드 수)만큼 보정 해준다.  

(ex) 1011111, 이미 7개이므로 보정 x
3. 해당 이진수의 정가운데 비트가 1인지 확인한다.  
   1. 1인 경우, 남은 양 쪽 비트를 확인하여 이 역시 이진트리인지 확인한다.
   2. 0인 경우, 해당 남은 비트들이 0인지 확인한다. (루트 노드가 0이면 그 밑의 리프 노드들은 모두 0이여야 함.)
   3. 아닌 경우, 포화 이진트리로 표현할 수 없다. False를 반환

(ex) 1011111의 왼쪽 트리, 가운데 노드, 오른쪽 트리는 각각 101 , 1, 111  
가운데 노드 = 1, 101(왼쪽 트리), 111(오른쪽 트리)도 위와 같은 과정 반복  

101의 가운데 노드가 0이고 이 아래 노드들이 모두 0이 아니므로 답이 False
4. 비트 수가 1일 때까지 반복

~~~
def solution(numbers):
    answer = []
    check = []
    for i in range(1, 7):
        check.append(2**i-1)

    for number in numbers:
        ten_num = ten_to_binary(number)
        if check_binary(ten_num, check):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def ten_to_binary(number):
    result = []
    while number >= 2:
        number, remain = divmod(number, 2)
        result.append(remain)
    else:
        result.append(number)
    return result[::-1]


def check_binary(number, check):
    for c in check:
        if len(number) == c:
            break
        elif len(number) < c:
            number = [0]*(c-len(number)) + number
            break
    if len(number) == 1:
        return True

    mid = (len(number)-1)//2
    if number[mid] == 0 and sum(number) > 0:
        return False
    if check_binary(number[:mid], [mid]) and check_binary(number[mid+1:], [mid]):
        return True
~~~