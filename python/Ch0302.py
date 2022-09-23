# 큰 수의 법칙
# n, m, k를 입력받는다 (숫자의 갯수, 총 연산 횟수, 연속된 숫자 제한 갯수)
n, m, k = map(int, input().split())

nArr = list(map(int, input().split()))

# 가장 큰 수와 두번째로 큰 수를 저장한다.
max_num = max(nArr)

max_index = nArr.index(max_num)

max_num2 = max(nArr[:max_index] + nArr[(max_index+1):])

total = 0
count_num = k + 1
div_num = m // count_num
div_num2 = m % count_num

total = ((div_num * ((max_num * k) + max_num2)) + (div_num2 * max_num))
print(total)

# 이코테 제공 풀이코드
# n, m, k = map(int, input().split())
# x = list(map(int, input().split()))
#
# x.sort()
# first = x[n - 1]
# second = x[n - 2]
#
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
#
# result = 0
# result += (count) * first
# result += (m-count) * second
#
# print(result)