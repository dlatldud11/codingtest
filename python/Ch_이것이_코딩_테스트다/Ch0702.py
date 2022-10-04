n = int(input())
arr = list(map(int, input().split()))

m = int(input())
cust = list(map(int, input().split()))

arr = sorted(arr)
# print(arr)
def find(x,y, item):
    # print(x,y,item)
    for i in arr[x:y]:
        # print(i)
        if i == item:
            return arr.index(i)
            break
    return -1

x = 0
y = len(arr)
for i in range(len(cust)):
    index = find(x,y,cust[i])
    # print(index)
    if(index > -1):
        print('true', end = ' ')
        if (i != len(cust)-1 and cust[i] < cust[i + 1]):
            x = index
        else:
            y = index
    else:
        print('false', end=' ')



