n, k = map(int, input().split())
list = [0]*n
for i in range(n):
    num = int(input())
    list[i] = num

list.sort(reverse=True)
count = 0
for i in list:
    count += k // i
    k %= i
print(count)