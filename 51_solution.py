# 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240
from collections import deque


# 인덱스 0은 물
def solution(food):
    result_list = deque([0])
    for idx in range(len(food) - 1, 0, -1):
        if food[idx] // 2 > 0:
            food_count = food[idx] // 2
            result_list.append(str(idx) * food_count)
            result_list.appendleft(str(idx) * food_count)

    result_list = ''.join(map(str, result_list))
    return result_list
