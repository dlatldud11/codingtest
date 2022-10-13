import sys
# 08 그래프이론 41 여행 계획

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 연결된 간선이 있는 노드 2개에 대해 union 연산 수행
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plans = list(map(int, input().split()))
# 여행 계획에 있는 도시들의 루트노드가 같은지 확인
result = True
for i in range(m-1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i+1]):
        result = False

if result:
    print('YES')
else:
    print('NO')