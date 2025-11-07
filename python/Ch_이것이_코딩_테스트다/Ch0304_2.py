# 그리디 기출문제 04 만들 수 없는 금액
# 내 풀이: 1부터 차례대로 증가하면서 가장 큰 화폐 단위부터 나누어떨어지도록 해보기..?
# 
n = int(input()) #리스트의 건수
nums = list(map(int, input().split()))
nums.sort()

target = 1
for i in nums:
    if(i > target):
        break
    else:
        target += i

print(target)

# 오답임. 깨우친 부분: 화폐의 최소단위인 1부터 시작하는 것이고 내가 가지고 있는 동전의 최소 단위 + 1 부터 다시 만들 수 있는지를
# 검증하기때문에 target-1 까지는 만들 수 있다고 설명하는 것임
