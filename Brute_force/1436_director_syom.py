# 첫 번째 실수: 6이 "연속해서" 3번 이상 나오는 것을 그냥 6이 3개 이상 있으면 된다고 이해(꼼꼼하게 읽자고!)
# 두 번째 에러: 시간초과(브루트포스 알고리즘의 경우, 연산량이 많아질 수 있어 시간초과가 되는지 잘 확인할 것)
n = int(input())
end_of_the_world = []
for num in range(666, 10000666):
    num_str = str(num)
    if '666' in num_str:
        end_of_the_world.append(num)
print(end_of_the_world[n-1])
