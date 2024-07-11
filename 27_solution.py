def solution(phone_number):
    replace_num = list(phone_number[:-4])
    result = []
    for i in range(len(replace_num)):
        result.append('*')

    result = ''.join(result)
    answer = result + phone_number[-4:]
    return answer


print(solution('0123456789'))

