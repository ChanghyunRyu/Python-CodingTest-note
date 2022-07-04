# 시간을 고려해서 readline()을 사용했는데 
# readline()의 경우, \n까지 저장하는 것을 명심하고 사용할 것
# 해당 사항때문에, 오류가 꽤 많이 일어났음
import sys

n, m = map(int, input().split())
pokemon_dic = {}
for i in range(n):
    pokemon = sys.stdin.readline()
    pokemon_dic[pokemon] = i + 1
    pokemon = pokemon.replace('\n', '')
    pokemon_dic['{}\n'.format(i+1)] = pokemon

answers = []
for j in range(m):
    question = sys.stdin.readline()
    answers.append(pokemon_dic[question])

for answer in answers:
    print(answer)
