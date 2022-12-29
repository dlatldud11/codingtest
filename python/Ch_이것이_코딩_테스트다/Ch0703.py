# 이코테 이진 탐색 떡볶이 떡 만들기
# 절단기 설정 높이를 이진 탐색으로 찾아가는 로직으로 만들기

# n, m 입력받기 떡의 개수 요청한 떡의 길이
n, m = map(int, input().split())

# 떡의 길이 리스트 arr 입력 받기
arr = list(map(int, input().split()))


# print(n, m, arr)
def binary(arr, target, left, right):
    middle = (left + right) // 2
    answer = 0
    for i in arr:
        if i - middle >= 0:
            answer += (i - middle)

    # print(answer, middle, target, left, right)
    if answer == target:
        return middle
    elif answer < target:
        return binary(arr, target, left, middle - 1)
    elif answer > target:
        return binary(arr, target, middle + 1, right)
    else:
        return -1


n = binary(arr, m, 0, max(arr))
print(n)