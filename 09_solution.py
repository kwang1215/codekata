def solution(n):
    answer = 0
    while True:
        if not 0 < n <= 1000:
            break

        if n % 2 == 0:
            answer += n
            n -= 2
        else:
            n -= 1

        if n < 0:
            break
    return print(answer)

solution(10)
solution(4)
solution(3)
