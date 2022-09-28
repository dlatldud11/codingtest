from collections import deque
import sys
input = sys.stdin.readline

# 15. 특정 거리의 도시 찾기, 백준 18352번
# n, m, k, x 입력받기 노드, 간선, 거리정보, 시작노드
n, m, k, x = map(int, input().split())

# INF = 1e9
# 노드별 최단거리 리스트 만들기
distance = [-1] * (n+1)

# 간선 리스트 만들기
road = [[] for _ in range(n+1)]

# 간선 정보 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

# 큐 선언하고 x 초기화 하기
q = deque([x])
distance[x] = 0

while q:
    now = q.popleft()
    for i in road[now]:
        if distance[i] == -1:
            q.append(i)
            distance[i] = distance[now] + 1

count = 0
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        count += 1
if count == 0:
    print(-1)