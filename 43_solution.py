# 크기가 작은 부분 문자열
def solution(t, p):
    number_list = []
    count = 0
    for i in range(len(t)):
        if len(t[i:i + len(p)]) < len(p):
            continue
        number_list.append(t[i:i + len(p)])

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
