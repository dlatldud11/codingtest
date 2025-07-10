# 입력값 받기
# DFS로 연결된 컴퓨터의 수를 카운팅 하기 마지막에 -1 (자기자신) 하기?

n = int(input()) #컴퓨터의수
m = int(input()) #컴퓨터 쌍의 수

visited = [False] * (n + 1) #방문체크용
g = [[] for _ in range(n+1)] #이중배열 그래프

# print(visited, g)

for i in range(m):
    x, y = map(int, input().split())
    # print(x, y)
    g[x].append(y)
    g[y].append(x)

cnt = 0
    
def dfs(g, index, visited):
    visited[index] = True
    
    global cnt
    cnt += 1
    # print(f"방문함 {index} {cnt}")
    
    for i in g[index]:
        if visited[i] is not True:
            dfs(g, i, visited)
                
dfs(g, 1, visited)

print(cnt-1)