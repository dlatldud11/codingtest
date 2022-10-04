# 이코테 04 두 배열의 원소 교체
# n, k를 입력받는다 리스트의 길이, 최대 바꿔치기 횟수
n, k = map(int, input().split())

# n만큼 반복하여 a, b리스트를 만든다

a = list(map(int, input().split()))

b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순 정렬을 해준다
b = sorted(b, reverse=True)
a.sort()

count = 0
while count < k:
    if a[count] < b[count]:
        count += 1
    else:
        break

for i in range(count):
    # print(a[i], b[i])
    a[i], b[i] = b[i], a[i]

print(sum(a))

