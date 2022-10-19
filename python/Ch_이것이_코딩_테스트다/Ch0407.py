# 이코테 구현 Ch0407 럭키스트레이트
# n 입력받기 점수(항상 짝수)
n = input()
# print(n[:len(n) // 2])
# n을 반으로 나눈 값을 비교하기
sF = n[:len(n) // 2]
sS = n[len(n) // 2:]
nF = 0
nS = 0
# print(int(i) for i in sF)
for i in sF:
    nF += int(i)

# print(nF)

for i in sS:
    nS += int(i)

if nF == nS:
    print('LUCKY')
else:
    print('READY')

# 풀이와 다른 점 풀이는 반으로 나눈 값을 변수로 두고
# 두개의 for문을 돌렸으며 0~ 반값, 반값~끝값
# 으로 더해서 비교를 했다