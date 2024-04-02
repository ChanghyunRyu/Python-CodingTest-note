# 동적 계획법(Dynamic Programming)

## 등장 배경

- 동적 계획법에 대하여 알아보기에 앞서 동적 계획법 줄여서 DP의 등장 배경부터 알아보겠습니다.  
  등장 배경을 설명하기 위해 자주 등장하는 피보나치 수열을 예로 설명해보겠습니다.  
  일반적으로 간단하게 피보나치 수열을 코드로 작성하면 다음과 같이 재귀함수를 사용하게 됩니다.
  
```python
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

- 그러나 다음과 같이 재귀함수를 사용할 경우 다음과 같은 문제점이 발생합니다.  

<img src="https://user-images.githubusercontent.com/83490220/179691368-c2160d1f-6293-42cc-a506-abddf6623149.png">

위의 그림에서는 피보나치(3)을 두번 계산하게 되지만 숫자 n이 커질수록 중복 계산하는 횟수는 기하급수적으로 늘어납니다.  
이러한 문제점을 해결하기 위해서 등장한 것이 동적 계획법입니다.

## 설명

- 주어진 문제를 해결하기 위해서, 문제를 하위 문제로 나누어 푼 다음, 그것을 결합하여 최종적인 목표를 달성하는 것이다. 
    

- 각 하위 문제의 해결을 계산한 뒤, 그 해결책을 저장하여 후에 같은 하위 문제(위의 경우, Fibo(3)이 이에 해당) 나왔을 경우  
다시 계산작업을 거치는 않는 형태로 해결한다. 풀어서 설명하자면 답을 계속해서 재활용하는 것이다.
  
  
- 이러한 동적 계획법을 통해 피보나치 수열을 푸는 경우 다음과 같다.
```python
def dynamic_fibonacci(n):
    fibo = [0]*n
    fibo[0] = fibo[1] = 1
    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n-1]
```

피보나치 수열의 재귀함수와 동적 계획법의 실행 횟수가 궁금하면 24416번 문제를 참고하면 된다.  
30의 경우; 재귀함수: 832040번, 동적계획법: 28번

---

### Problem solved

- [**1로 만들기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/made_one)
