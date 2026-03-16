# 백준 2178 미로 탐색 260313
# 문제에서 bfs라고 했으므로 bfs로 풀이 진행
# 26.03.26 지금까지 dfs로 풀고 있었음 bfs로 다시 변경하기 변경하고 최단경로의 건수를 카운팅하는 방식을 바꿔서 진행하기
from collections import deque
import sys

def bfs(list, i, j):
    q = deque()

    q.append((i,j))
    list[i][j] = '0'
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        # print(f'bfs 실행됨 {x} {y}')

        for a in range(4):
            mx = x + moveX[a]
            my = y + moveY[a]

            if -1 < mx < n and -1 < my < m and list[mx][my] == '1':
                q.append((mx,my))
                list[mx][my] = '0'
                visited[mx][my] = visited[x][y] + 1

moveX = [1, -1, 0, 0] #오른쪽 왼쪽 위 아래
moveY = [0, 0, 1, -1] #오른쪽 왼쪽 위 아래

n, m = map(int, input().split())

arr = [list(list(sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0 for col in range(m)] for row in range (n)]


bfs(arr, 0, 0)
# print(visited)
print(visited[n-1][m-1])

