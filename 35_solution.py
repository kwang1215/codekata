# 부족한 금액 계산하기

def solution(price, money, count):
    total = 0
    for num in range(count):
        total += price * (num + 1)

    if total <= money:
        answer = 0
    else:
        answer = total - money

    return answer


print(solution(3,20,4))
print(solution(100,500,4))




