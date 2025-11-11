from collections import deque
import sys

def bfs(g, a, b):
    # print(f'bfs 들어옴 a: {a} b: {b}')
    q = deque([(a,b)])
    cnt = 0

    if g[a][b] == '1':
        g[a][b] = '0'
        cnt += 1

    while q:
        x, y = q.popleft()

        for i in range(len(xa)):
            if( x + xa[i] > -1 and x + xa[i] < n and y + ya[i] > -1 and y + ya[i] < n):
                if g[x + xa[i]][y + ya[i]] == '1':
                    q.append((x + xa[i], y + ya[i]))
                    g[x + xa[i]][y + ya[i]] = '0'
                    cnt += 1

    return cnt

# 백준 2667 단지번호 붙이기
# 인풋을 받아서 for문 안에서 입력값 받고 리스트로 만들어주기
n = int(sys.stdin.readline()) #반복값
arr = [] #지도
cnts = [] #단지수 담을 리스트

for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

xa = [0, 0, -1, 1] #상하좌우
ya = [1, -1, 0, 0] #상하좌우

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            cnts.append(bfs(arr, i, j))

cnts.sort()
print(len(cnts))
for i in cnts:
    print(i)
