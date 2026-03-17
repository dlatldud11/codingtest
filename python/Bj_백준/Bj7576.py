# 백준 7576 토마토
# 260317 일단 BFS를 구현하고 그 구현해서 어떻게 진행이 되는지 확인 해보기
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        day = arr[y][x]

        for k in range(4):
            mx = x + wx[k]
            my = y + wy[k]

            if -1 < mx < m and -1 < my < n and arr[my][mx] == 0:
                 arr[my][mx] = day + 1
                 q.append((mx, my))


m, n = map(int, input().split()) #가로칸, 세로칸
arr = [list(map(int, input().split())) for _ in range(n)] #배추의 위치

wx = [0, 0, -1, 1] #상하좌우
wy = [-1, 1, 0, 0] #상하좌우

q = deque()

for y in range(n): #행
    for x in range(m): #열
        if arr[y][x] == 1:
            q.append((x, y))

bfs()

# 0이 있으면 -1 리턴, 최댓값이 1이면 0 리턴 그 외에는 최대값 -1 리턴
has_zero = any(0 in row for row in arr)

if has_zero:
    print(-1)
else:
    print(max(map(max, arr)) -1)