# 이코테 연산자 끼워넣기 260324
# 백준 14888번 두번째 풀음
# n입력받기, arr입력받기, add, min, mul, div 입력받기
# 랜덤 호출로 dfs를 계속 구현하기

# 풀이 확인함. 모든 경우의 수를 방문하는 경우로 진행이 필요해보임
# 백준으로 맞춘 다음에 코드 gpt한테 검사받고 다시 더 효율 좋은코드로 만듬
def dfs(index, rst):
    global max_rst, min_rst
    # print(f'dfs {index} {rst}')

    if index == n:
        max_rst = max(max_rst, rst)
        min_rst = min(min_rst, rst)
        return
    
    for i in range(4):
        if signs[i] > 0:
            signs[i] -= 1

            if i == 0:
                # add
                dfs(index + 1, rst + arr[index])
            elif i == 1:
                # min
                dfs(index + 1, rst - arr[index])
            elif i == 2:
                # mul
                dfs(index + 1, rst * arr[index])
            elif i == 3:        
                # div
                if rst < 0:
                    dfs(index + 1, -(-rst // arr[index]))
                else:
                    dfs(index + 1, rst // arr[index])
            signs[i] += 1

n = int(input())
arr = list(map(int, input().split()))
signs = list(map(int, input().split()))
max_rst = -1000000000 #최대값
min_rst = 1000000000 #최소값

dfs(1, arr[0])

print(max_rst)
print(min_rst)