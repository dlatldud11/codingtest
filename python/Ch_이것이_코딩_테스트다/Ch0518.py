# Ch05 DFS/BFS Q18 괄호변환

# 1. 균형잡힌 괄호문자열을 만드는 재귀함수 만들기
# 2. 호출한 뒤 올바른 괄호문자열을 확인하는 로직을 호출해서 로직에 따라 1.을 호출하기

def balance(str):
    chk = 0
    for i in range(len(str)):
        if (len(str) == 0 or i > 0) and chk == 0:
            return(str[:i], str[i:])
        
        if str[i] == '(':
            chk -= 1
        else:
            chk += 1
    return(str, "")
        
def correct(str):
    # print(f'correct 들어옴 {str}')
    u, v = balance(str)
    # print(f'u {u}, v {v}')
    if u[0] == '(':
        if v == '':
            return u
        else:
            rst = correct(v)
            return u + rst
    else:
        if v == '':
            return '(' + v + ')' + change(u[1:-1])
        else:
            rst = correct(v)
            return '(' + rst + ')' + change(u[1:-1])
        
def change(str):
    answer = ''
    for i in range(len(str)):
        if str[i] == '(':
            answer += ')'
        else:
            answer += '('
    return answer

w = input() #입력받은 문자열
# u, v = balance(w)
# print(f'u {u}, v {v}')

str = correct(w)

print(f'str {str}')