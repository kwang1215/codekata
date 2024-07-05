def solution(numbers):
    sum = 0
    for number in numbers:
        sum += number

    answer = sum / len(numbers)
    return print(answer)

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])