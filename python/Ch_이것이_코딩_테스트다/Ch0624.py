# 이코테 국영수
# n을 입력받는다, 학생 수
n = int(input())
# 이름, 국어, 영어, 수학 순으로 입력을 받는다 리스트에 넣는다
arr = []

for i in range(n):
    arr.append(list(input().split()))

# 리스트를 정렬한다

arr = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in arr:
    print(i[0])