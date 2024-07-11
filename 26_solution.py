# 음양 더하기
def solution(absolutes, signs):
    result = []
    for i, sign in enumerate(signs):
        if sign == True:
            result.append(absolutes[i])
        else:
            result.append(-(absolutes[i]))
    answer = sum(result)
    return answer
