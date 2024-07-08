def solution(x, n):
    answer = []
    count = 0
    sum = x

    while True:
        answer.append(sum)
        sum += x
        count += 1
        if count == n:
            break
    return answer

for i in solution(-4,2):
    print(i)