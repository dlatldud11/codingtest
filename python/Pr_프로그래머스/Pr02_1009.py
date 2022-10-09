# 프로그래머스 2단계 221009 피보나치 수

def solution(n):
    answer = 0
    dp = [0] * (n+1)
#     dp 0,1초기화
    for i in range(2):
        dp[i] = i

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i - 2]
# print(dp)
    answer = dp[n] % 1234567
    return answer

print(solution(3))