def solution(n):
    factor = n
    answer = 0
    while factor > 0:
        if n % factor == 0:
            answer += factor
            factor -= 1
        else:
            factor -= 1
    return print(answer)

solution(12)
solution(5)