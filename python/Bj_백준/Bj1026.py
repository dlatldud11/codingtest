# 보물
cnt = int(input()) #리스트 건수 받기
alist = list(map(int, input().split(' '))) #A리스트
blist = list(map(int, input().split(' '))) #B리스트

alist.sort()
blist.sort(reverse=True)

# print(cnt)
# print(alist)
# print(blist)

answer = 0

answerlist = [alist[i] * blist[i] for i in range(cnt)]

print(sum(answerlist))