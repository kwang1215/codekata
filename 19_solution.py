def solution(n):
    n = n ** (1 / 2)
    if n % 1 == 0:
        answer = (n + 1) ** 2
        return answer
    else:
        answer = -1
        return answer


s1 = solution(121)
print(s1)
s2 = solution(3)
print(s2)
