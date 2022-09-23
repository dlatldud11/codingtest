# 이코테 왕실의 나이트
n = input()
# ord char -> int a == 97 이므로 y축과 맞춰서 1~8 로 되게끔 만듬
x, y = ord(n[0]) - 96, int(n[1])

dx = [2, -2, 1, -1]
dy = [1, -1]

count = 0
for i in dx:
    for k in dy:
        if abs(i) % 2 == 1:
            k *= 2
        sum_x, sum_y = x+i, y+k
        if sum_x > 0 and sum_x < 9 and sum_y > 0 and sum_y < 9:
            count += 1

print(count)

# 책 풀이
# 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)
