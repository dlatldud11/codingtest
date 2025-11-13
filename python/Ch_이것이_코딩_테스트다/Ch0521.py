import sys
from collections import deque
# 이코테 05. BFS DFS 21.인구 이동 백준 16234번

# bfs를 결과 건이 없을 때 까지 호출하기. 땅의 인구수를 업데이트 하는 로직 만들기
# 맨처음 푼 로직은 시간초과가 됨 맨 마지막에 다시 전체를 돌면서 인구수 업데이트를 하는데서 시간초과가 나는 것 같음
n, l, r = map(int, sys.stdin.readline().split()) #대지칸수, 최소인구, 최대인구
arr = [] #인구수 담은 지도

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

xa = [0, 0, -1, 1] #상하좌우
ya = [-1, 1, 0, 0] #상하좌우
answer = 0 #일수

def bfs(x, y):
    sum = arr[x][y] #인구수 누적합
    visited[x][y] = 1 #방문처리
    union = [(x,y)] #연합정보

    q = deque([(x, y)])

    while q:
        a, b = q.popleft()

        nowh = arr[a][b] #현재 위치의 인구수
        for i in range(4):
            if (a + xa[i] < n and a + xa[i] > -1 and b + ya[i] < n and b + ya[i] > -1):
                if visited[a + xa[i]][b + ya[i]] == 0: #방문한 적 없는 땅이라면
                    nearh = arr[a + xa[i]][b + ya[i]] #근방의 위치의 인구수

                    if abs(nowh - nearh) >= l and abs(nowh - nearh) <= r:
                        visited[a + xa[i]][b + ya[i]] = 1 #방문처리
                        q.append((a + xa[i], b + ya[i]))
                        union.append((a + xa[i], b + ya[i]))
                        sum += nearh
    return union, sum

while(True):
    visited = [[0] * n for _ in range(n)]
    unions = [] #연합된 좌표와 합계
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                union, sum = bfs(i,j)
                if len(union) > 1:
                    unions.append((union, sum))
    
    if not unions:
        print(answer)
        break

    # 한번의 bfs 이후 국경 연 나라들끼리 인구수 나누어 담기
    for union, sum in unions:
        renew = sum // len(union)
        # print(f"renew {renew}")
        for x, y in union:
            arr[x][y] = renew

    answer += 1 #일수 증가
