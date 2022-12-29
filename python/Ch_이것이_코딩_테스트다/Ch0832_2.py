# 다이나믹 프로그래밍 Ch0832 정수 삼각형
n = int(input())
arr = [[] for _ in range(n)]
d = [[0] * n for _ in range(n)]

for i in range(n):
    narr = list(map(int, input().split()))
    arr[i] = narr
    # if i < n - 1:
    # arr[i].add(0 * (n - 1 - i))

for i in range(n):
    if i == 0:
        d[0][i] = arr[0][0]
    else:
        d[0][i] = 0

# print(arr)
for i in range(1, n):
    for k in range(len(arr[i])):
        if k < 1:
            d[i][k] = d[i - 1][k] + arr[i][k]
        else:
            d[i][k] = max(d[i - 1][k - 1], d[i - 1][k]) + arr[i][k]

print(max(d[n - 1]))