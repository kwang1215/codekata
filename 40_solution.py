# 3진법 뒤집기
def solution(n):
    num_list = []
    answer_list = []
    count = 0

    while n > 0:
        if n % 3 == 0:
            num_list.append(0)
        else:
            num_list.append(n % 3)
        n = n // 3

    for num in reversed(num_list):
        answer_list.append(num * (3 ** count))
        count += 1
    return sum(answer_list)
