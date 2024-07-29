# 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(month, day):
    year = 2016
    # 만약 월이 1월이나 2월이면, 전년도 13월과 14월로 변환합니다.
    if month == 1 or month == 2:
        month += 12
        year -= 1

    # Zeller의 공식 적용
    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

    # 요일을 구합니다.
    days_of_week = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
    return days_of_week[h]