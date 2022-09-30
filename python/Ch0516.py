import sys
#이코테 연구소
#1. N, m을 입력받는다 행,열
n, m = map(int, input().split())

#2. Arr 지도 리스트를 만든다.
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

# arr의 바이러스가 퍼진 모습을 담을 temp 리스트
temp = [[0] * m for _ in range(n)]

result = 0

# 바이러스 전파시키는 함수
def virus(x, y):
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if  0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 0을 카운팅하는 함수
def counting():
    score = 0
    for i in range(n):
        for k in range(m):
            if temp[i][k] == 0:
                score += 1
    return score

#3. 벽 3개를 만드는 함수
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for k in range(m):
                temp[i][k] = arr[i][k]

        for i in range(n):
            for k in range(m):
                if temp[i][k] == 2:
                    virus(i, k)

        result = max(result, counting())
        return

    for i in range(n):
        for k in range(m):
            if arr[i][k] == 0:
                arr[i][k] = 1
                count += 1
                dfs(count)
                arr[i][k] = 0
                count -= 1

dfs(0)
print(result)


# for i in range(n):
#     for k in range(m):
#         if arr[n][m] == 0:

# 정답 풀이
# import sys
#
# n, m = map(int, input().split())
# data = []
# temp = [[0] * m for _ in range(n)]
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0 , 0]
#
# result = 0
# # 1. 바이러스가 전파시키는 DFS 함수
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)
#
# # 2. 안전영역 계산하는 함수
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
#
# # 3. 벽 설치하는 모든 경우의 수 탐색하면서 안전영역 계산
# def dfs(count):
#     global result
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#
#         for i in range(n):
#             for j in range(m):
#                 # 바이러스면 전파 수행
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         # 안전영역 계산
#         result = max(result, get_score())
#         return
#
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
#
# dfs(0)
# print(result)

