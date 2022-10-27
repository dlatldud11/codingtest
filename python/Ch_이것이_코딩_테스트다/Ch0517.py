from collections import deque
import sys

# 풀이 본 후 바이러스를 큐에 담아서 bfs를 수행한다
# 바이러스 종류, 시간, x좌표, y좌표

# 이코테 경쟁적 전염 Ch0517 백준 18405
# n, k 입력받기 시험관칸수, 바이러스종류
n, k = map(int, sys.stdin.readline().split())

# arr 입력받기 시험관 리스트
arr = []

# 바이러스 종류, 시간, x좌표, y좌표 정보
virus = []

# 상하좌우 좌표값
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for k in range(n):
        if arr[i][k] != 0:
            virus.append([arr[i][k], 0, i, k])

virus.sort()

# print(virus)
# s, x, y 입력받기  시간초, x좌표, y좌표
s, x, y = map(int, sys.stdin.readline().split())

q = deque(virus)

while (q):
    v, ns, nx, ny = q.popleft()
    # print(q)
    if s == ns:
        break
    for i in range(4):
        ndx = nx + dx[i]
        ndy = ny + dy[i]
        if 0 <= ndx < n and 0 <= ndy < n:
            if arr[ndx][ndy] == 0:
                arr[ndx][ndy] = v
                q.append([v, (ns + 1), ndx, ndy])

print(arr[x - 1][y - 1])