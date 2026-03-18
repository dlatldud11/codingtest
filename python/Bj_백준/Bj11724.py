# 백준 11724 연결 요소의 갯수
# DFS 문제라고 나와있어서 그 방식대로 해결해보기
# 계속 틀린 이유 양방향 그래프로 만들어야했는데 그러지 못했음
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(i):
    for j in arr[i]:
        if visited[j] == False:
            visited[j] = True
            dfs(j)

n, m = map(int, input().split())

visited = [False for _ in range(n+1)] #방문처리
arr = [[] for _ in range(n+1)] #그래프

for i in range(m):
    y, x = map(int, input().split())
    arr[y].append(x)
    arr[x].append(y)

cnt = 0
for i in range(n):
    if visited[i+1] == False:
        visited[i+1] = True
        dfs(i+1)
        cnt +=1

print(cnt)
