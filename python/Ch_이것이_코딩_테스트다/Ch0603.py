# chapter06 정렬
# 실전문제 3. 성적이 낮은 순서로 학생 출력하기


# n을 입력받는다
n = int(input())

# arr를 만든다. 만든 리스트를 정렬한다. (조건부 정렬) 하고 프린트 한다.
arr = [ input().split() for _ in range(n)]

arr.sort(key=lambda x:int(x[1])) #숫자 변환해야 정확한 정렬이 가능!

for std, grd in arr:
    print( std, end=' ')