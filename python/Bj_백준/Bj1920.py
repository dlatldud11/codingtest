# 백준 1920 수 찾기  260326
# 못풀음 시간초과를 생각하기. 교집합은 한번만 만든다. for문 밖에서 set1.intersection(set2) 이런식으로
# 교집합 만들었어도 됐고 아니면 그냥 n 리스트를 처음부터 set으로 만들어서 비교했어도 됐다.

n = int(input())
nSet = set(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

for i in mArr:
    if i in nSet:
        print(1)
    else:
        print(0)