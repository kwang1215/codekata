def solution(n):
    answer = 1
    while True:
        if n % answer == 1:
            return print(answer)
        else:
            answer += 1

solution(10)
solution(12)