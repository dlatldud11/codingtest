# 백준 2108 통계학

# 최빈값 리스트 만드는 함수(최빈값이 1개 이상일 때 리스트의 형태로 리턴)
# def modefinder(numbers):
#     c = Counter(numbers)
#     order = c.most_common()
#     maximum = order[0][1]

#     modes = []
#     for num in order:
#         if num[1] == maximum:
#             modes.append(num[0])
#     return modes

import sys
input = sys.stdin.readline
n = int(input())
arr = []
count = dict()
arrSum = 0
maxvalue = -4000
minvalue = 4000

for i in range(n):
    m = int(input())
    arr.append(m)
    arrSum += m

    maxvalue = max(maxvalue, m)
    minvalue = min(minvalue, m)

    if m not in count:
        count[m] = 1
    else:
        count[m] += 1

arr.sort()

# 산술평균, 중앙값, 최빈값, 범위
print(round( arrSum /n))

print(arr[n//2])

freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])    

print(maxvalue - minvalue)