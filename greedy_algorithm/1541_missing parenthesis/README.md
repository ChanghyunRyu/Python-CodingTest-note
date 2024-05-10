## 잃어버린 괄호

------

[백준 1541번] 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 세준이는 괄호를 모두 지웠다.  
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.  
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
- 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
- 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

### 출력

- 첫째 줄에 정답을 출력한다.

------

### Problem Solved Check

- [x] 1회 24/05/10
- [ ] 2회
- [ ] 3회

### 풀이

문제에서 제시하는 식은 '-', '+'로만 이루어진다.  
식의 값을 최소로 만들기 위해서는 '-' 기호 뒤에 있는 수들을 최대한 크게 만들어야 한다.  
'-' 기호 뒤의 수들을 최대한 크게 만들기 위해서는 '-' 기호 뒤의 수들을 괄호를 통해서 더해야 한다.  
여기서 '-' 뒤의 수는 최대한 커져야 하기 때문에 괄호에 '-' 기호는 포함 시키지 않는다.  
즉, - 기호 뒤에서 괄호를 시작하여 그 다음 - 앞에서 괄호를 끝내는 것이다.
  
예시를 통해 설명하면,
다음과 같은 식이 입력으로 들어왔다고 생각한다.

55-50+40+90-20+80

위에서 설명한대로 이 식에 괄호를 적용하게되면

55-(50+40+90)-(20+80)

이처럼 '-' 기호 뒤에서 ( 가 시작되어 그 다음 '-' 기호가 나오기 전 )로 끝나게 된다.

괄호는 다음과 같이 추가한다고 해석을 했다면 다음 문제는 이를 어떻게 파이썬 문법으로 구현할 것인가 이다.  
사실 이는 훨씬 간단하게 구현된다. 위와 같이 괄호를 추가한다고 가정할 경우, '-' 기호가 나온 이후 모든 수들은 결과값을 구할 때 빼기를 한다고 생각하면 되기 때문이다.

~~~
equation = input()

result = 0
start = 0
minus = False
for i in range(len(equation)):
    if equation[i] == '-' or equation[i] == '+':
        number = int(equation[start:i])
        start = i+1
        if minus:
            result = result - number
        else:
            result = result + number
        if equation[i] == '-':
            minus = True
        continue
    if i == len(equation) - 1:
        number = int(equation[start:i+1])
        if minus:
            result = result - number
        else:
            result = result + number
        if equation[i] == '-':
            minus = True
print(result)
~~~
~~~
line = input()
result = 0
start = 0
minus = 1

for i in range(len(line)):
    if line[i] == '+' or line[i] == '-':
        number = int(line[start:i])
        result += minus*number
        start = i+1
    elif i == len(line)-1:
        number = int(line[start:i+1])
        result += minus * number
        start = i + 1
    if line[i] == '-':
        minus = -1
print(result)

~~~
