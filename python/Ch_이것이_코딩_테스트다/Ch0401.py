# 이코테 구현 01상하좌우

# n 입력 받기
# 계획서 리스트 받기
# 최종적으로 도착할 좌표 구하기
# ex) n=5 계획서 R R R U D D 답 3,4

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
ax, ay = 1, 1

directs = list(map(str, input().split(' ')))

# print(directs)

for key in directs:
    if key == 'L':
        ax += dx[0]
        ay += dy[0]
    elif key == 'R':
        ax += dx[1]
        ay += dy[1]
    elif key == 'U':
        ax += dx[2]
        ay += dy[2]
    else:
        ax += dx[3]
        ay += dy[3]

    if ax > n:
        ax = n
    elif ax < 1:
        ax = 1
    if ay > n:
        ay = n
    elif ay < 1:
        ay = 1

print(ay, ax)

# 풀이 확인
# input().split() 해도 문자열로 공백 기준으로 리스트로 만들어줌
# 문자열 순서와 x, y좌표 증가량 순서를 일치하게 해서
# 이중 포문 안에서 값이 증가되도록 만들었다.

plans = input().split()
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            x = ax + dx[i]
            y = ay + dy[i]
    if x > n or x < 1 or y > n or y < 1:
        continue
    else:
        dx = x
        dy = y

# 이런 식으로 진행되도록 했다.