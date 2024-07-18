# 크기가 작은 부분 문자열
def solution(t, p):
    number_list = []
    count = 0
    for i in range(len(t)): # 문자열 t만큼의 길이만큼 반복문 실행
        # 문자열 t의 인덱스i부터 인덱스 i+ 문자열 p의 길이만큼의 단어가 문자열 p의 길이보다 작을 경우 반복문 재시작
        if len(t[i:i + len(p)]) < len(p):
            continue
        # 문자열 t의 첫 인덱스 부터 i+p의 길이 만큼 슬라이싱 한후 넘버리스트에 저장
        number_list.append(t[i:i + len(p)])

    # 슬라이싱한 번호들 문자열p와 크기 비교 후 조건이 맞을 때 카운트에 추가
    for num in number_list:
        if int(num) <= int(p):
            count += 1
    return count


t = "3141592"
p = "271"
t = "500220839878"
p = "7"
t = "10203"
p = "15"
print(solution(t, p))
