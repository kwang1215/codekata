# 수박수박수박수박수박수?
def solution(n):
    result = []
    for i in range(n):
        if (i + 1) % 2 == 1:
            result.append('수')
        else:
            result.append('박')

    str_result = ''.join(result)
    return str_result


print(solution(3))
print(solution(4))