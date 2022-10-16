#프로그래머스 2단계 멀리 뛰기

def solution(n):
    answer = 0
    d = [0] * 2001
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        d[i] = d[i - 1] + d[i - 2]

    answer = d[n] % 1234567
    return answer