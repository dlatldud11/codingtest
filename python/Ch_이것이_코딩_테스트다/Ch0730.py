# Ch0730 가사탐색
def solution(words, queries):
    answer = []

    for q in queries:
        cnt = 0
        getSe(q)
        # print(q, start, end)
        for w in words:
            if start == 0:
                if len(w) == len(q) and q[end + 1:] == w[end + 1:]:
                    cnt += 1
            else:
                if len(w) == len(q) and q[:start] == w[:start]:
                    cnt += 1
        answer.append(cnt)

    return answer


def getSe(query):
    global start
    global end
    start = None
    for i in range(len(query)):
        if query[i] == '?':
            if start == None:
                start = i
            end = i
    return

    # 위는 내가 적은 오답 정답은 맞았는데 효율성에서 오답이 나왔다.


from bisect import bisect_left, bisect_right


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word)  # 단어를 삽입
        reversed_array[len(word)].append(word[::-1])  # 단어를 뒤집어서 삽입
    for i in range(10001):  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:  # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?':  # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:  # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        # 검색된 단어의 개수를 저장
        answer.append(res)

    return answer

    # 위는 정답 코드

    # 이거 같다... 이중 배열은 단어 갯수 별로 모으려고 한 것 같고
    # 이중 배열 별로 정렬을 한 것은 각 단어를 사전순으로 정렬하기 위함이다(접미사는 정렬이 반대순이여야 하므로 단어를 거꾸로 넣은 것임)
    # 그 뒤 ?를 a로 바꾼 문자열과 z로 바꾼 문자열을 비슷한 문자열로 묶이는 것의
    # 처음과 끝이 되도록 만들어서
    # bisect 라이브러리를 이용해서 뽑아낸 것이다