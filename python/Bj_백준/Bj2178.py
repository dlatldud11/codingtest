# 백준 2178 미로 탐색 260313
# 문제에서 bfs라고 했으므로 bfs로 풀이 진행
from collections import deque
import sys



def bfs(list, i, j):

    q = deque()
    if i < 0 or i >= n or j < 0 or j >= m:
        print(f'올바른 값이 아님 {i} {j}')
        pass

    if list[i][j] == '1':
        list[i][j] = '0'
        # q.append()


n, m = map(int, input().split())

arr = [list(list(sys.stdin.readline().strip())) for _ in range(n)]

print(arr)

bfs(arr, n, m)
    

