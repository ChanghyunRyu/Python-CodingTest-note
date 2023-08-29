n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

answer = (m//(k+1))*((k*first)+second) + (m%(k+1))*first
print(answer)
