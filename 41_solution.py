# 이상한 문자 만들기
def solution(s):
    s_list = s.lower()
    answer = []
    idx = 0

    for word in s_list:
        if idx % 2:
            answer.append(word)
        else:
            answer.append(word.upper())
        idx += 1
        if word == ' ':
            idx = 0
    return (''.join(answer))