# 백준 그리디
# 못 품 풀이 참고하기
# 11
# 1 4 -> 3
# 3 5 -> 2
# 0 6 -> 6
# 5 7 -> 2
# 3 8 -> 5
# 5 9 -> 4
# 6 10 -> 4
# 8 11 -> 3
# 8 12 -> 4
# 2 13 -> 9
# 12 14 -> 2

# 풀이 참고
# 끝나는 시간 기준으로 정렬을 해야 함. 이유는 끝나는 시간이 이르면 뒤에 배치할 회의를 더 많이 생각 할 수 있으므로
# 따라서 먼저 시작시간으로 오름차순 정렬 한 뒤, 끝나는 시간으로 다시 오름차순 정렬을 해준다.

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda a: a[0]) #시작시간 기준 오름차순
time = sorted(time, key=lambda a: a[1]) #끝나는시간 기준 다시 오름차순

# print(time)

last = 0
count = 0

for i, j in time:
    if i >= last:
        count += 1
        last = j

print(count)