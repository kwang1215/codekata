# 약수의 개수와 덧셈

def solution(left, right):
    measure_list = []
    for num in range(left, right + 1):
        n = 1
        measure = []
        for i in range(num):
            if num % n == 0:
                measure.append(n)
            n += 1
        if len(measure) % 2 == 0:
            measure_list.append(num)
        else:
            measure_list.append(-num)

    return sum(measure_list)

print(solution(13, 17))
print(solution(24, 27))