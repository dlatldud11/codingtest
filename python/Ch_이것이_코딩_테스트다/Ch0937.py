# 이코테 09. 최단거리 37. 플로이드 백준 11404

import sys

INF = int(1e9)

# n을 입력받는다. 도시의 개수

n = int(input())

# m을 입력받는다. 버스의 개수

m = int(input())

# fee 리스트를 만든다. 행(도시의 개수) 열(버스의 개수)

fee = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 0으로 초기화해주는 부분

for i in range(1, n + 1):

    for k in range(1, n + 1):

        if i == k:
            fee[i][k] = 0

# x번 도시에서 시작해서 y번 도시까지 가는 버스의 비용 z를 담는 리스트가 필요함

# print(fee)

for i in range(m):

    # x 출발도시 y 도착도시 z 비용

    x, y, z = map(int, input().split())

    if fee[x][y] == INF:

        fee[x][y] = z

    else:

        fee[x][y] = min(z, fee[x][y])

# print(fee[1:])

# 예시 1번 마을에서 출발해서 2번 마을로 도착하는 경우의 수 1.다이렉트로 가는 방법 2.하나의 마을을 거쳐 가는 방법

for k in range(1, n + 1):  # 거치는점

    for i in range(1, n + 1):  # 시작점

        for j in range(1, n + 1):  # 끝점

            if fee[i][j] > fee[i][k] + fee[k][j]:
                fee[i][j] = fee[i][k] + fee[k][j]

for k in range(1, n + 1):

    nstr = ''

    for i in range(1, n + 1):

        if fee[k][i] == INF:

            nstr += str(0) + ' '

        else:

            nstr += str(fee[k][i]) + ' '

    print(nstr[:-1])

# print(fee)



