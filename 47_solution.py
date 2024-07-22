# 문자열 내 마음대로 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    # 1. 각 문자열의 n번째 문자를 기준으로 정렬 기준 리스트 생성
    sort_criteria_list = []
    for word in strings:
        sort_criteria_list.append((word[n], word))

    # 2. 정렬 기준 리스트를 정렬
    sort_criteria_list.sort()

    # 3. 정렬된 리스트에서 원래 문자열만 추출
    sorted_strings = []
    for criteria in sort_criteria_list:
        sorted_strings.append(criteria[1])

    return sorted_strings
