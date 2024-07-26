# 명에의 전당
# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    result = []
    for idx in range(len(score)):
        sorted_score = sorted(score[:idx + 1], reverse=True)
        result.append(min(sorted_score[:k]))
    return result


print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))