# 백준 1439 뒤집기
# 인터넷 풀이를 보니까 0으로만드는 경우와 1로 만드는 경우 중
# 최솟값을 출력한다.


# 인풋을 먼저 받는다 (문자열 배열?)
arr = str(input())

# 0과 1인 경우 뒤집는 카운팅용 리스트
ran = [0] * 2 
nums = ["0", "1"]

for n in nums:
    for i in range(len(arr)):
        # print(f"i: {i}  arr[i]:  {arr[i]}  len(arr):  {len(arr)}")
        if(arr[i] != n):
            if(i == len(arr) -1):
                ran[int(n)] += 1
                continue
            if(arr[i+1] != n):
                continue
            else:
                ran[int(n)] += 1

print(min(ran))