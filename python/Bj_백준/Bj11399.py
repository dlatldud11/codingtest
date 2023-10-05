# 백준 그리디 문제
# 11399

# 배열이 들어오면 오름차순으로 정리한다.
# 답 배열을 만든다
# for문으로 답 배열에 값을 넣어주고 합계를 또 넣어준다
# 답을 출력할때는 합계를 출력한다.

num = int(input())
arr = list(map(int, input().split()))
addArr = [0] * num

arr.sort()
# print(arr)

for i in range(num):
    if i > 0:
        addArr[i] = arr[i] + addArr[i-1]
    else:
        addArr[i] = arr[i]

# print(addArr)
print(sum(addArr))
