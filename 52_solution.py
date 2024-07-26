# a = 3
# b = 1
# n = 20
#
# first = (n // a) * b + (n % a)
# print(first)
# second = (first // a) * b + (first % a)
# print(second)
# third = (second // a) * b + (second % a)
# print(third)
#
# answer = ((n // a) * b) + ((first // a)) + ((second // a))

# 콜라 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a,b,n):
    return_coke = 0
    while n >= a:
        return_coke += (n // a) * b
        n = (n % a) + (n // a) * b
    return return_coke


print(solution(2,1,20))
