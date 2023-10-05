# 백준 그리디 설탕 배달 2839

# 5를 먼저 나누고 나머지를 구한다
# 나머지를 3으로 나눈 다음에 나머지를 구한다.

# 못 풀음 풀이 참고함

n = int(input())
answer = 0

while n >= 0:
    if n % 5 == 0:
        answer += int(n // 5)
        print(answer)
        break

    n -= 3
    answer += 1

else:
    print(-1)


