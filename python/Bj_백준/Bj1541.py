# 잃어버린 괄호
inp = input()
minsplit = inp.split('-')
# print(minsplit)

answer = 0

for a in range(len(minsplit)):
    plusanswer = 0 #+끼리 먼저 합친 값
    # print(a)
    plusplit = minsplit[a].split('+')

    intplus = map(int, plusplit)
    plusanswer = sum(intplus) 
    # print(plusanswer)

    if a == 0:
        answer = plusanswer
    else:
        answer -= plusanswer

# print("누적값")
print(answer)