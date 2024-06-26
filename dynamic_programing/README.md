# 동적 계획법(Dynamic Programming)

---

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

<img src="https://user-images.githubusercontent.com/83490220/179691368-c2160d1f-6293-42cc-a506-abddf6623149.png" height="300">

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

### 최장 증가 부분 수열 알고리즘(LIS, Longest Increasing Subsequence)

원소 N개를 가진 어떤 임의의 배열이 있을 때, 일부 원소들을 골라내서 만든 부분 수열 중, 
각 원소가 이번 원소보다 크다는 조건을 만족하는(즉, 오름차순으로 정렬된) 수열 중에서 가장 긴 수열을 **최장 증가 부분 수열** 이라고 한다.  

LIS는 동적 계획법으로 풀 수 있는 대표적인 알고리즘으로 다음과 같은 방법들로 구할 수 있다.

- **방법1. O(N^2):** dp[i] = A[i] (i번째 원소)를 마지막 값으로 가진 가장 긴 LIS를 저장한다. A[i]가 수열에 반드시 포함되어야 하기 때문에 A[0]~A[i-1] 중 A[i]보다 작은 값을 가진 부분 수열을 찾아야한다.


  1. 0번째~(i-1)번째 수열을 탐색 A[i]보다 작은 원소를 가진 수열 중 가장 긴 수열의 길이를 구한다. (즉, A[i] > A[k]를 만족하는 k 중 가장 큰 dp[k]를 구하면 된다.)
  2. 이를 수열 끝까지 반복하여 모든 dp[i]를 구한다.
  3. dp[i] 중 가장 큰 값을 반환한다.


- **방법2. O(NlogN):** 위의 방법 1은 시간복잡도가 O(N^2)으로 동작 속도가 느리다. 이는 이분 탐색을 활용하여 해결할 수 있다. 
기존 LIS를 저장하는 dp 배열 외에 dp[j] = k를 만족하는 j 중에서 A[j] 값이 가장 작은 j를 따로 저장해놓는 것이다.


  1. 현재 i번째 원소를 탐색하고 있다고 가정한다. 그리고 가장 작은 j를 저장하고 있는 배열 B가 있다고 한다. B[k] = k길이의 수열 중 마지막 숫자가 가장 작은 수열의 마지막 숫자
2. 만약 A[i]가 B의 마지막 원소보다 크다고 한다면 B 끝에 A[i]를 삽입하고 dp[i] = B의 길이가 된다. 만약 크지 않다면 이진탐색을 이용하여 B에서 A[i]의 위치를 탐색한다.
3. 탐색하여 나온 위치가 k라고 했을 때, dp[i] = B[k]가 된다. 또한 A[i] < B[k]이면 B[k]를 A[i]로 최신화해준다.
4. 이를 수열 끝까지 반복한 후, B의 최종 크기를 반환하면 된다.

[**Python을 이용한 LIS 구현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/11053_longest_subsequence)

---

### 다양한 동적 계획법 최적화 방법

- **Knuth's Optimization**

---

### Problem solved

- [**1로 만들기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/made_one)
- [**개미 전사**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/ant_warrior)
- [**등굣길**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/on_the_way_to_school)
- [**N으로 표현**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/expression_n)
- [**도둑질**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/thief)
- [**1149번 RGB 거리**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/1149_RGB_street)
- [**1904번 01타일**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/1904_01_tile)
- [**1912번 연속합**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/1912_continuous_sum)
- [**1932번 정수 삼각형**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/1932_integer_triangle)
- [**2156번 포도주 시식**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/2156_wine_tasting)
- [**2565번 전깃줄**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/2565_power_cord)
- [**2597번 계단 오르기**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/2579_climbing_stairs)
- [**9251번 LCS**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/9251_LCS)
- [**11049번 행렬 곱셈 순서**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/11049_matrix_multiplication_order)
- [**11053번 가장 긴 증가하는 부분 수열**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/11053_longest_subsequence)
- [**11054번 가장 긴 바이토닉 부분 수열**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/11054_longest_bitonic_subsequence)
- [**11055번 가장 큰 증가하는 부분 수열**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/11055_biggest_subsequence)
- [**12865번 평범한 배낭**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/12865_plain_backpack)
- [**24416번 알고리즘 수업 1 - 피보나치 수열**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/dynamic_programing/24416_algorithm_class_fibonacci_num_1)
