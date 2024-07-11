# 핸드폰 번호 가리기

# def solution(phone_number):
#     replace_num = list(phone_number[:-4])
#     result = []
#     for i in range(len(replace_num)):
#         result.append('*')
#
#     result = ''.join(result)
#     answer = result + phone_number[-4:]
#     return answer

def solution(numbers):
    answer = '*' * len(numbers[:-4]) + numbers[-4:]
    return answer


print(solution('01042069433'))