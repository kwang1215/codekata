def solution(num1, num2):
    answer = num1 - num2
    return print(f'num1이 {num1}이고 num2가 {num2}이므로 {num1} - {num2} = {answer}')

num1 = int(input("첫번째 숫자입력"))
num2 = int(input("두번째 숫자입력"))
solution(num1,num2)