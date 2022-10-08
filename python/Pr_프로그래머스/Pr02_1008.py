# 프로그래머스 2단계 JadenCase 문자열 만들기
def solution(s):
    #     대문자 65 90 / 소문자 97 122 / 숫자 48 57 / 공백 32
    # print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'), ord(' '))

    answer = ''
    #     공백이 연속으로 나오면 처음 나온 공백 다음 공백은 리스트에 들어감
    strArr = s.split(' ')
    # print(strArr)
    ns = ''
    for nstr in strArr:
        if len(nstr) == 1:
            nstr = nstr[0].upper()
        elif len(nstr) > 1:
            nstr = nstr[0].upper() + nstr[1:].lower()
        answer += nstr + ' '

    answer = answer[:-1]
    return answer