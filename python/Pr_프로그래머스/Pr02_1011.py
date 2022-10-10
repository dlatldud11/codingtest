# 프로그래머스 2단계 카펫
def solution(brown, yellow):
    answer = []
#     가로 >= 세로 일 때 까지 가로 //2 세로 *2 한 다음 값을 대입해보기
    v = yellow #가로
    h = 1 #세로

    while(v >= h):
        r = v + 2
        c = h + 2
        square = r * c
        print(v,h)
        if square == brown + yellow:
            answer = [r, c]
            break
        # elif brown < square - yellow:
        else:
            while True:
                h += 1
                if yellow % h == 0:
                    v = yellow // h
                    break
    return answer