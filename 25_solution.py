def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    result.sort()
    if not result:
        result.append(-1)
    return result
