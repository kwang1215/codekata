# 최대공약수와 최소공배수
def solution(n, m):
    min_num = min(n, m)
    max_num = max(n, m)

    answer = []

    for i in range(1, min_num + 1):
        if min_num % i == 0 and max_num % i == 0:
            max_measure = i

    min_multiple = int(abs(min_num * max_num) / max_measure)
    answer.append(max_measure)
    answer.append(min_multiple)
    return answer

print(solution(2,5))
print(solution(3,12))
print(solution(6,4))