def solution(x):
    list_x = list(str(x))
    sum = 0
    for num in list_x:
        sum += int(num)

    if x % sum == 0:
        return True
    else:
        return False