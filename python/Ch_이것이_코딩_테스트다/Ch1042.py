import time

start = time.time()
# 그냥 중복되는 수 제외하고 말하면 안되나..?
# 이코테 그래프 이론 탑승구
# 방문처리 해주기?
# g 입력받기 탑승구의 수a
g = int(input())

# p입력받기 비행기의 수
p = int(input())

parent = []
for i in range(g + 1):
    parent.append(i)

# print(parent)
# 주차현황 garr 만들기
garr = [0] * (g + 1)


# find_parent 함수 만들기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union_parent 함수 만들기
def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


count = 0
# 입력 받는 순서대로 도킹하고 카운팅하기
for i in range(p):
    nx = find_parent(parent, int(input()))
    if nx == 0:
        break
    else:
        union_parent(parent, nx, nx - 1)
        count += 1

print(count)

# 풀이를 설명해준 블로그 글을 보고 나서야 이해가 되었다
# 도킹 가능한 최대 탑승구에 도킹한다고 가정하고 해당 탑승구에 비행기를 도킹했으면
# 동일한 탑승구까지 도킹 가능한 비행기는 그보다 한 칸 작은 탑승구에 도킹할 수 있으므로
# 루트 노드를 자기 자신이 아닌 자신보다 1 작은 탑승구로 세팅한다
# 더 이상 탑승할 수 없는 상태 0이 될 때 깨제 반복한다.


# print(time.time() - start)