# 이코테 10.그래프 이론 44. 행성 터널 2887번
import sys
# n 입력받기. 행성의 갯수
n = int(sys.stdin.readline())

# 행성 위치 정보 담는 리스트
p = []


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
    return

parent = [0] * n

for i in range(n):
    parent[i] = i

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    p.append([x, y, z])

# print(p)
cost = []

for i in range(n):
    for k in range(n):
        if i != k:
            ncost = min(abs(p[i][0] -p[k][0]) , abs(p[i][1] - p[k][1]), abs(p[i][2]- p[k][2]))
            # print(ncost)
            cost.append((ncost, i, k))


cost = sorted(cost)
# print(cost)
count = 0
for i in range(len(cost)):
    z, a, b = cost[i]
    # print(a, b, z)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        count += z

print(count)

