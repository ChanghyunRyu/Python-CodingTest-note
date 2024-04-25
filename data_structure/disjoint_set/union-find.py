# 노드와 간선 입력
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i


# find 연산 즉, 해당 노드의 루트 노드 찾기
# 이는 해당 노드가 어떤 집합에 속해 있는지(정확히는 속한 집합의 루트 노드를) 확인할 수 있다.
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x


# union 연산 즉, 두 노드의 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(e):
    x, y = map(int, input().split())
    union_parent(x, y)

print('각 원소가 속한 집합:', end=' ')
for i in range(1, v+1):
    print(find_parent(i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
