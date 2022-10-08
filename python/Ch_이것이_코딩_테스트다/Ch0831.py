# 이코테 다이나믹프로그래밍 금광
# t를 입력받는다. 테스트케이스
t = int(input())

# t for문 안에서 n, m을 입력받는다. 행 열
for nt in range(t):
    n, m = map(int, input().split())

#   인풋으로 들어오는 문자열로 arr를 만든다.
    arr = []
    strArr = list(map(int, input().split()))
    for i in range(n):
        start = (i * m)
        end = (i * m) + m
        arr.append(strArr[start:end])
    # print(arr)

# d 리스트를 만든다 이중배열
    d = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            d[r][c] = arr[r][c]
    # print(d)

    for c in range(1, m):
        for r in range(n):
            # print(r, c)
            if r == 0:
                d[r][c] = max(d[r][c-1], d[r+1][c-1]) + d[r][c]
            elif r == (n-1):
                d[r][c] = max(d[r-1][c-1], d[r][c-1]) + d[r][c]
            else:
                d[r][c] = max(d[r-1][c-1], d[r][c-1], d[r+1][c-1]) + d[r][c]

    nmax = 0
    for r in range(n):
        nmax = max(d[r][m-1], nmax)

    print(nmax)