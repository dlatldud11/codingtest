# 28. 고정점 찾기
#n을 입력받는다
n = int(input())

#arr를 입력받는다
arr = list(map(int, input().split()))

#이진탐색을 수행한다
def binary_search(arr, x, y):
    # print(x, y)
    if x > y:
        return -1
    # z = ((y - x) // 2) + x
    z = (x + y) // 2

    # print(arr[z], z)
    if arr[z] == z:
        return z
    elif arr[z] < z:
        return binary_search(arr, z + 1 , y)
    else:
        return binary_search(arr, x, z - 1)

print(binary_search(arr, 0, len(arr)-1))

# 내가 다른 점 처음에 x > y 만 if문으로 안에 넣으면 되고 return 값으로는 None을 해주면 된다.
# z = ((y - x) // 2) + x 이런 식으로 두 값의 중간 지점을 구했는데 (x + y) // 2 이렇게 계산해주는게 정석인 것 같다.
# 그리고 이진탐색을 호출할 때도 len() -1 해준다.
# 그리고 처음 if문 세팅으로 None을 해주었기 때문에 index 변수를 둬서 print 해준다.