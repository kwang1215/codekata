def solution(n):
    answer = 0
    n=list(str(n))
    for i in range(len(n)):
        n[i] = int(n[i])
        answer += n[i]
    return print(answer)

solution(123)
solution(987)