def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


# 이코테 Ch1043 어두운 길
# 최소 신장트리 만드는 문제
# n, m을 입력받는다 집의 수 도로의 수
n, m = map(int, input().split())

parent = []
for i in range(n):
    parent.append(i)
# print(parent)

# 간선의 비용 담는 리스트
line = []

for i in range(m):
    x, y, z = map(int, input().split())
    line.append((z, x, y))

line = sorted(line)

# 총 비용 담는 변수
answer = 0
total = 0
for i in line:
    z, x, y = i
    # print(z, x, y)
    nx = find_parent(parent, x)
    ny = find_parent(parent, y)
    total += z
    if nx != ny:
        union_parent(parent, x, y)
        answer += z

print(total - answer)

# 오답노트 최소신장트리를 구하는데 필요한 리스트는
# 2개 뿐이다 parent와 비용 순으로 정렬 된 간선 리스트
# 답안은 총값 - 최소 값 이다.
