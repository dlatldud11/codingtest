# 이코테 06정렬 25 실패율
# n 입력받기 스테이지의 갯수
n = int(input())

# stages 입력받기 사용자의 현재 스테이지상태
stages = list(map(int, input().split()))

# 실패율 담는 리스트
arr = []
for i in range(1, n + 1):
    # print(i)
    p = 0  # 스테이지 통과한사람
    s = 0  # 스테이지 머무르는사람
    for stage in stages:
        if i <= stage:
            p += 1
        if i == stage:
            s += 1
    if p == 0:
        r = 0
    else:
        r = s / p
    arr.append((r, i))

arr = sorted(arr, key=lambda x: (-x[0], x[1]))
# print(arr)

for i in arr:
    print(i[1], end=' ')
    # answer.append(i[1]) 프로그래머스용 답안
