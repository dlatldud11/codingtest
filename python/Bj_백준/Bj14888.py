import sys
# 풀이 생각못함
# dfs를 활용해서 재귀적으로 모든 경우의 수를 계산해내고 마지막에 최솟값과 최댓값을 추출
# !!!처음 답지 배꼈을 때 틀린 점: dfs를 호출하고 나서는 다시 -1 했던 부호들을 원복 해줘야함...

n = int(sys.stdin.readline()) #숫자의 갯수
arr = list(map(int, sys.stdin.readline().split()))

plus, minus, multiple, divide = map(int, sys.stdin.readline().split())

min_value = int(1e9) 
max_value = -int(1e9)

def dfs(i, now):
    global min_value, max_value, plus, minus, multiple, divide

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1   
            dfs(i+1, now + arr[i])
            plus += 1   
        if minus > 0:
            minus -= 1
            dfs(i+1, now - arr[i])
            minus += 1
        if multiple > 0:
            multiple -= 1
            dfs(i+1, now * arr[i])
            multiple += 1
        if divide > 0:
            divide -= 1
            dfs(i+1, int(now/arr[i]))
            divide += 1

dfs(1, arr[0])

print(max_value)
print(min_value)