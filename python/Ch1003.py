# 그래프 이론 - 도시 분할 계획
# n, m을 입력받는다. (집의 갯수, 길의 갯수)
n, m = map(int,input().split())

#  도로리스트를 만든다
cost = [] * m

# parent 리스트를 만든다.
parent = [0] * (n+1)
for i in range(1, n+1):
   # print(i)
    parent[i] = i

# print(parent)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 이진트리를 만드는 함수에 cost값 넣어주는 로직도 추가해준다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

# m만큼 반복하면서 최소신장트리를 만드는 함수를 호출한다.
for _ in range(m):
    # a, b 집 c 비용
    a, b, c = map(int, input().split())
    cost.append((c, a, b))

# cost를 정렬한다.
cost.sort()

total = 0;
max_cost = 0;
for i in cost:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        total += i[0]
        max_cost = i[0]

print(total - max_cost)
