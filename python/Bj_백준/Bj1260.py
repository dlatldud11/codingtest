from collections import deque

# 정점, 간선, 시작번호 인풋받기
n, m, start = map(int, input().split())

bfs_visited = [False] * (n + 1) #방문확인용
dfs_visited = [False] * (n + 1) #방문확인용
g = [[] for _ in range(n+1)]#그래프

answer = [[] for _ in range(2)]

for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x) #양방향 그래프
    
g = [sorted(adj) for adj in g]

def dfs(g, index, visited):
    # print(index, end=' ')
    answer[0].append(index)
    visited[index] = True
    
    for i in g[index]:
        if visited[i] is False:
            dfs(g, i, visited)


def bfs(g, index, visited):
    #첫번째 노드를 덱에 삽입하고 방문처리한다.
    # 첫번째 노드에 인접한 노드를 모두 순서대로 덱에 삽입하고 방문처리한다.
    # 끝나면 덱에서 popleft로 꺼내와서 다시 반복한다.
    d = deque()
    d.append(index)
    visited[index] = True
    
    while d:
        chk = d.popleft()
        # print(chk, end=' ')
        answer[1].append(chk)
        for i in g[chk]:
            if visited[i] is False:
                d.append(i)
                visited[i] = True

dfs(g, start, dfs_visited)
bfs(g, start, bfs_visited)

print(*answer[0])
print(*answer[1])

