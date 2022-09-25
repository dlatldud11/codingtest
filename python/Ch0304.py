# 1이 될 때 까지
# n 입력되는 수 k 나누기 할 때 나누어떨어져야 하는 수 입력받기
n, k = map(int, input().split())
answer = 0
while n > 1:
    if n % k == 0:
        n = n // k
    else:
        n -= 1
    answer += 1

print(answer)

# 교재 정답
# N, K공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)