def solution(numbers):
    good_number = [0,1,2,3,4,5,6,7,8,9]
    sum_number = []
    for number in good_number:
        if not number in numbers:
            sum_number.append(number)
    answer = sum(sum_number)
    return answer


print(solution([5,8,4,0,6,7,9]))


