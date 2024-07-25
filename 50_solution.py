# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    find_duplicate_list = []
    for i, word in enumerate(s):
        if word in find_duplicate_list:
            idx = i
            count = 0
            while True:
                count += 1
                idx -= 1
                if word == s[idx]:
                    answer.append(count)
                    break
        else:
            find_duplicate_list.append(word)
            answer.append(-1)

    return answer