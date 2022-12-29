# 이코테 정렬 24 안테나
# 가장 합한 거리가 적은 부분을 찾기. 집이 있는 위치에 하나의 안테나를 설치하고 안테나 끼리의 거리를 측정하기
# 총 집의 갯수가 최대 200000, 거리는 100000이므로 같은 집이 있는 거리부터 계산을 해보기

# n을 입력받기, 집의 수
# n = int(input())
#
# # distance array를 입력받기 집의 위치
# distance = list(map(int, input().split()))
#
# # print(distance)
# # count dictionary 만들기
# count = {}
#
# for i in range(len(distance)):
#     if count.get(distance[i]) == None:
#         count[distance[i]] = 1
#     else:
#         count[distance[i]] += 1
#
# min = 200000 * 100000
# maxnum = max(list(count.values()))
#
#
# def countL(x, count):
#     sum = 0
#     for i in list(count.keys()):
#         sum += (abs(x - i) * count.get(i))
#
#     print(sum)
#     return
#
#
# countL(0, count)
# answer = -1
#
# for d in list(count.keys()):
#     sum = 0
#     for k in list(count.keys()):
#         sum += (abs(d - k) * count.get(k))
#
#         # print(sum)
#     if sum < min:
#         min = sum
#         answer = d
#
# print(answer)

# 시간초과

# 교재풀이

n = int(input())
house = sorted(list(map(int, input().split())))

print(house[(n-1)//2]) # 중앙값


