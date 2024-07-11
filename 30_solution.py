# 가운데 글자 가져오기
def solution(words):
    if len(words) % 2 == 1:
        answer = words[(len(words) // 2)]
    else:
        answer = words[(len(words) // 2 - 1): (len(words) // 2 + 1)]
    return answer


print(solution('abcde'))
print(solution('qwer'))




