# 이코테 6-2 위에서 아래로
# n을 입력받는다. 주어지는 수열의 개수
n = int(input())

# arr를 만들고 n만큼 반복해서 값을 넣어준다.
arr = []
for i in range(n):
    arr.append(int(input()))

# arr.sort(reverse=True)
arr = sorted(arr, reverse=True)

for i in arr:
    print(i)