import sys
from itertools import combinations

# 못품 풀이를 본 후 다시 작성해보기
# 이코테 DFS/BFS 20. 감시 피하기 백준 18428 번과 동일한 문제
# 1. 학생을 감지하는 함수
# 2. 장애물 3개를 순열로 만드는 파이썬 라이브러리로 리스트 만들기
# 3. 모든 선생님에 대해 학생을 감지할수있는지를 확인하는 함수

n = int(sys.stdin.readline()) #지도 칸수
arr, teachers, halls = [], [], [] #지도, 선생님, 복도 위치리스트

for i in range(n):
    row = list(sys.stdin.readline().split())
    arr.append(row)

    for j in range(n):
        if(row[j] == 'T'):
            teachers.append((i,j)) #선생님 위치 저장
        if(row[j] == 'X'):
            halls.append((i,j)) #복도 위치 저장

def find_student(x, y, d):

    if(d == 0): #동
        while(y < n):
            if(arr[x][y] == 'O'):
                return False
            elif(arr[x][y] == 'S'):
                # print(f"{x}{y}에 학생 있음! {d}")
                return True
            y += 1
        return False
    if(d == 1): #서
        while(y > -1):
            if(arr[x][y] == 'O'):
                return False
            elif(arr[x][y] == 'S'):
                # print(f"{x}{y}에 학생 있음! {d}")
                return True
            y -= 1
        return False
    if(d == 2): #남
        while(x < n):
            if(arr[x][y] == 'O'):
                return False
            elif(arr[x][y] == 'S'):
                # print(f"{x}{y}에 학생 있음! {d}")
                return True
            x += 1
        return False
    if(d == 3): #북
        while(x > -1):
            if(arr[x][y] == 'O'):
                return False
            elif(arr[x][y] == 'S'):
                # print(f"{x}{y}에 학생 있음! {d}")
                return True
            x -= 1
        return False


def check():
    for x, y in teachers:
        # print(f"{x} {y}")
        for i in range(4):
            if(find_student(x, y, i)):
                # print(f"학생을 찾을 수 있으므로 검색을 끝냄! {x}, {y}, {i}")
                return False
            
    return True


blocks = list(combinations(halls, 3)) #3개의 방해물을 조합으로 생성

answer = "NO"

for block in blocks:
    for x, y in block:
        arr[x][y] = 'O' #방해물 설치
    
    if(check()):
        # print("YES")
        answer = "YES"
        break

    for x, y in block:
        arr[x][y] = 'X' #방해물 원복


print(answer)