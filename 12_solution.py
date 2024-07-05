def solution(arr):
    sum = 0
    for num in arr:
        sum += num
    answer = sum/len(arr)
    return print(answer)

solution([1,2,3,4])
solution([5,5])