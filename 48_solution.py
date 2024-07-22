# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    command_list = []
    for command in commands:
        i, j, k = command
        command_list.append(sorted(array[i - 1: j])[k - 1])
    return command_list