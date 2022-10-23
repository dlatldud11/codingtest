# 이코테 구현 Ch0408 문자열 뒤집기
# s 입력받기 (문자열)
s = input()
# 숫자일 시 더할 변수
n = 0
# 문자열일 시 담을 리스트
arr = []

# 49 ~ 58 숫자 65 ~ 알파벳 대문자
for i in s:
    #  print(ord(i), i)
    if 48 <= ord(i) <= 58:
        n += int(i)
    else:
        arr.append(i)

# print(arr, n)

arr.sort()
arr.append(str(n))
print(''.join(arr))

# 오늘 배운 것 join 함수 구분자.join(리스트)