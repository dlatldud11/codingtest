# 3. 게임 개발
#1. N,m,d 을 입력받는다 행, 열, 현재방향 list를 뺀다
n, m  = map(int, input().split())

# 2. 좌표를 입력받는다
x, y, d = map(int, input().split())

# 3. 방향순서 , dx, dy를 만든다 북0 동3 남2 서1
turn = [0, 3, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 4.맵의 정보를 입력받는다
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 5. While문 안에서 회전하고 회전한 방향에 맞는 방향의 arr를 확인하는 등의 로직을 구현한다 -> count = 1로 수정
turn_time = 0
count = 1

while True:
    #현재 위치 방문처리
    arr[x][y] = 1
    # 왼쪽으로 회전
    d += 1
    turn_time += 1
    if d > 3:
        d = d % 4
    if turn_time == 5:
        nx = x - dx[d]
        ny = y - dy[d]
        turn_time = 0
    else:
        nx = x + dx[d]
        ny = y + dy[d]
    # print(nx, ny, arr[nx][ny], turn_time)
    if arr[nx][ny] == 0:
        count += 1
        arr[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        # print(arr)
    elif turn_time == 0:
        break

print(count)
