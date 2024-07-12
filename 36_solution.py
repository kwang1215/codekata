# 문자열 다루기 기본

def solution(a):
    list_a = list(a)
    list_num = list(range(0, 10))

    if len(a) == 4 or len(a) == 6 :
        for word in list_a:
            if word not in ''.join(map(str, list_num)):
                answer = False
                break
            else:
                answer = True
    else:
        answer = False

    return answer

s = '12345'
a = '2342'
print(solution(s))
print(solution(a))