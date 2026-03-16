# 백준 1012 유기농 배추
# 26.03.16 BFS로 풀어볼 생각임 !!!처음으로 풀이까지 다 생각해서 맞춘 것 같음!
# 챗gpt 의 피드백을 받고 필요 없는 로직을 덜어내고 다시 커밋함 (cnt필요 없음 방문처리 로직 바깥으로 뺌)
from collections import deque

def bfs(i, j):
    q = deque()
    if visited[j][i] == 1:
        visited[j][i] = 0
        q.append((i,j))

        while q:
            x, y = q.popleft()
            for v in range(4):
                mx = x + arrx[v]
                my = y + arry[v]
                
                if -1 < mx < m and -1 < my < n and visited[my][mx] == 1:
                    visited[my][mx] = 0
                    q.append((mx, my))

t = int(input()) #test case

arrx = [0 , 0, -1, 1] #상하좌우
arry = [-1 , 1, 0, 0] #상하좌우


for i in range(t):
    answer = 0 #정답건수
    m, n, k = map(int, input().split()) # 가로길이, 세로길이, 배추갯수
    visited = [[0 for col in range(m)] for raw in range(n)]

    cab = [tuple(map(int, input().split())) for _ in range(k)] #배추 있는 위치

    for j in cab:
       visited[j[1]][j[0]] = 1 #배추 있는 자리 방문여부에 남겨놓기

    for x, y in cab:
        if visited[y][x] == 1:
            bfs(x,y)
            answer += 1

    print(answer)