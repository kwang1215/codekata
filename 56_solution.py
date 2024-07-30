# 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    # 점수 내림차순으로 정렬
    score.sort(reverse=True)

    max_profit = 0
    # m개씩 묶어서 상자를 만들고 이익을 계산
    for i in range(0, len(score), m):
        if i + m <= len(score):
            # 현재 상자에서 가장 낮은 점수를 구함
            box = score[i:i + m]
            min_score_in_box = box[-1]
            max_profit += min_score_in_box * m

    return max_profit


# 예제 입력
k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
# k = 4
# m = 3
# score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
