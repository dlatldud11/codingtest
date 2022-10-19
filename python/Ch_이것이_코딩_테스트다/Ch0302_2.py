# 이코테 0302 곱하기 혹은 더하기
# s 입력받기 숫자 문자열 48 == 0
s = input()

result = 0
# for문을 돌리면서
for i in range(len(s)):
    # print(s[i], ord(s[i]), result)
    if 1 < int(s[i]):
        # 현재 번호 1 이상
        if result < 2:
            result += int(s[i])
        else:
            result *= int(s[i])
    else:
        # 현재 번호 0
        result += int(s[i])

print(result)

# 해설을 참고하였다 해설은 1을 기준으로 더하거나 곱할 것을 알랴주었다
# 플러스 괜히 ord() 안 써도 되었다