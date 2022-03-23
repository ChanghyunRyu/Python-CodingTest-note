a, b, c = map(int, list(input().split()))
# 노트북 생산 대수가 n 이라고 할때, a + b*n < c*n 인 가장 작은 n을 찾아야한다.
# a < c*n - b*n -> a < (c-b)n -> a/(c-b) < n
# 처음 디자인할 때, b=c 인 경우 대처를 하지 못 하여서 런타임 에러가 일어남!
if c == b:
    n = -1
else:
    n = (a//(c-b)) + 1
if n > 0:
    print(n)
else:
    print(-1)
