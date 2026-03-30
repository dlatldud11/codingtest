# 백준 10817 세 수 260330
# 리스트 입력 받고 정렬 한 다음에 두번째 것만 출력하기?

arr = list(map(int, input().split()))
arr.sort()
print(arr[1])