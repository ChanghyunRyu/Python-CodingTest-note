n = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))
result = 0
min_price = prices[0]
for i in range(len(lengths)):
    result += lengths[i]*min_price
    if min_price > prices[i+1]:
        min_price = prices[i+1]
print(result)
