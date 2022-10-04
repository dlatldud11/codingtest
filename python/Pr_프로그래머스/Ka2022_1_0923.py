# 카카오 2022 블라인드 코딩테스트 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    #     이름 : 순서 쌍 딕셔너리
    dic = {}
    #     신고 당한 횟수
    count = [0] * len(id_list)
    #     신고자, 신고한 사람 담은 리스트
    list = [[] for _ in id_list]
    #     몇번 메일 받았는지 세는 리스트
    new_answer = [0] * len(id_list)

    for i in range(len(id_list)):
        dic[id_list[i]] = i

    for j in report:
        name, call = j.split()
        name = dic.get(name)
        call = dic.get(call)

        if call in list[name]:
            continue
        else:
            count[call] += 1
            list[name].append(call)

    for m in range(len(count)):
        if count[m] >= k:
            for q in range(len(list)):
                if m in list[q]:
                    new_answer[q] += 1

    print(new_answer)

    answer = new_answer
    return answer