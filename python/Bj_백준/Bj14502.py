# 백준 14502 연구소
# 260317 예전에 실패로 끝난 문제를 다시 풀어보기 풀이를 기억했을 때 순열 등을 활용해야 풀 수 있었던 것으로 기억함

from itertools import combinations
from copy import deepcopy
from collections import deque

def bfs(i, j, war):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            mx = x + dx[k]
            my = y + dy[k]

            if -1 < mx < m and -1 < my < n and new_arr[my][mx] == 0 and (mx, my) not in war:
                new_arr[my][mx] = 2
                q.append((mx, my))


n, m = map(int, input().split()) #세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
wars = [(x, y) for y in range(n) for x in range(m) if arr[y][x] == 0] #벽인 경우의 좌표값 추출

dx = [0, 0, -1, 1] #상하좌우
dy = [-1, 1, 0, 0] #상하좌우
max_cnt = 0

for i in combinations(wars, 3):
    visited = [[0 for row in range(m)] for col in range(n)]
    new_arr = deepcopy(arr)
    for y in range(n):
        for x in range(m):
            if new_arr[y][x] == 2:
                bfs(x, y, i)

    max_cnt = max(max_cnt, sum(row.count(0) for row in new_arr) - 3)

print(max_cnt)