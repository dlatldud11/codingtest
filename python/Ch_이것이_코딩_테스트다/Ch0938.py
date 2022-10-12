# 이코테  0938 정확한 순위
# 플로이드 워셜 알고리즘을 활용해서 풀이 가능
# 경로를 설정해서 성적의 순위를 파악할 수 있게 함 a학생이 b보다 점수가 낮다면
# a에서 b로 가는 경로가 존재한다는 뜻

# n, m입력받기 학생수, 간선 수
n, m = map(int, input().split())

INF = int(1e9)

arr = [[INF] * (n + 1) for _ in range(n + 1)]
# 디폴트로 무한 값을 넣어 초기화
# 자기 자신은 0으로 세팅
for i in range(1, (n + 1)):
    for k in range(1, (n + 1)):
        if i == k:
            arr[i][k] = 0

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1

# print(arr)
# 플로이드 워셜 알고리즘을 수행(거쳐가는 값이 존재한다면 세팅)
for k in range(1, (n + 1)):
    for i in range(1, (n + 1)):
        for j in range(1, (n + 1)):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
# 각 행을 돌면서 값이 있는 경우를 카운팅하여서 총 학생수와 같다면 판단 가능

print(arr[1:])

answer = 0
for i in range(1, (n + 1)):
    count = 0
    for k in range(1, (n + 1)):
        if arr[i][k] != INF or arr[k][i] != INF:
            count += 1
    # print(count)
    if count == n:
        answer += 1

print(answer)