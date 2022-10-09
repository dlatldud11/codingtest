# 이코테 08 다이나믹 프로그래밍 32 정수 삼각형

# n을 입력받는다. 삼각형의 크기
n = int(input())

# for문을 돌려서 arr를 입력받는다.
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for r in range(n):
    for c in range(len(arr[r])):
        if len(arr[r]) < n:
            # print((n - len(arr[r])))
            for i in range(n - len(arr[r])):
                arr[r].append(0)
# print(arr)

# 이중 for문을 돌려서 dp를 수행한다 r먼저, c나중에
for r in range(1, n):
    for c in range(len(arr[r])):
        # print(r, c)
        if c == 0:
            arr[r][c] = arr[r-1][c] + arr[r][c]
        else:
            arr[r][c] = max(arr[r-1][c], arr[r-1][c-1]) + arr[r][c]

# nmax = 0
# for c in range(len(arr[n-1])):
#     nmax = max(arr[n-1][c], nmax)
#
# print(nmax)
print(max(arr[n-1]))
