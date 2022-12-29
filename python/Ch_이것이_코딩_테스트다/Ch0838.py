# 이코테 다이나믹 프로그래밍 38 퇴사
# 풀이 참고
# n 입력받기 퇴사일
n = int(input())

# 일자별 소요일, 금액 담아주는 리스트 생성 t, p
t = []
p = []

# 해당 일의 가장 큰 수익을 담을 dp 1차원 배열 선언
dp = [0] * (n + 1)

max_val = 0

for i in range(n):
    day, price = map(int, input().split())
    t.append(day)
    p.append(price)

# 거꾸로 반복문 돌리기
for i in range(n - 1, -1, -1):
    time = t[i] + i  # 해당 상담을 했을 시 종로되는 날짜
    if time <= n:

        max_val = max(p[i] + dp[time], max_val)
        dp[i] = max_val
        # 원래 풀이는 위에가 dp[i] 아래가 max_val
    else:
        dp[i] = max_val
    # print(dp)
print(max_val)