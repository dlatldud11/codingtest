n, m = map(int, input().split())

arr = []
result = 0
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    if arr[x][y] == 0 : #아직 방문이 안되어있으면
        arr[x][y] = 1
        # 상, 하, 좌, 우 방문하기
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    else:
        return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)