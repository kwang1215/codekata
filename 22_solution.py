def solution(a, b):
    sum = 0
    if a < b:
        x = a
        while True:
            sum += x
            x += 1
            if x == b:
                sum += x
                break
    elif b < a:
        x = b
        while True:
            sum += x
            x += 1
            if x == a:
                sum += x
                break
    else:
        sum = a

    return print(sum)


solution(3,5)
solution(3,3)
solution(5,3)
