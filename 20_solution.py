def solution(n):
    # int를 list화
    list_answer = list(map(int, str(n)))
    list_answer.sort(reverse=True)
    # int를 str로 변환한 뒤 list를 str화 후 다시 int화
    str_answer = int(''.join(str(s) for s in list_answer))
    return str_answer

solution(118372)
