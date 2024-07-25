# 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations


def solution(numbers):
    sum_list = []
    combi_num_list = list(combinations(numbers, 2))

    for combi in combi_num_list:
        if sum(combi) in sum_list:
            continue
        sum_list.append(sum(combi))

    answer = sorted(sum_list)
    return answer
