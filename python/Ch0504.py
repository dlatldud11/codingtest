#DFS/BFS 4.미로탈출
from collections import deque

def bfs(bx,by):
    q = deque([(bx, by)])
    count[bx][by] = 1

    while(q):
        x,y = q.popleft()

        arr[x][y] = 0 #방문처리

        countNum = count[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            # if(arr[nx][ny] == 0):
            #     continue
            if(arr[nx][ny] == 1):
                q.append((nx , ny))
                count[nx][ny] += (countNum + 1)
    return count[n-1][m-1]

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int,input())))

count = [[0]*m for _ in range(n)] #누적 담아주기 m가 가로(y) n이 세로(x)

# 이동할 방향 설정 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))