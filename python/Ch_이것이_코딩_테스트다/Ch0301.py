# Ch0301 이코테 그리디 모험가 길드
# n을 입력받는다 모험가의 수
n = int(input())

# arr를 만든다 모험가 리스트
arr = list(map(int, input().split()))

# print(arr)

arr = sorted(arr)
print(arr)
count = 0
result = 0
for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(count)

# 풀이를 보고 풀음 모험가를 오름차순으로 정렬
# 모험가를 한명 씩 확인하면서 그룹으로 묶은 인원수와 공포도가 일치하면
# 그룹 결성 후 인원수 다시 초기화
# 문제가 이해가 잘 안간다 인터넷에서 보니까 설명도 조금씩 달라서 교제로 다시 한 번 봐봐야 겠다