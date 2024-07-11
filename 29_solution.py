def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        answer = arr
    elif len(arr) == 1:
        answer = [-1]
    return answer


print(solution([10]))
