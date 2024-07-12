# 문자열 내림차순으로 배치하기

def solution(z):
    answer = ''.join(sorted(z, reverse=True))
    return answer

print(solution('Zbcdefg'))