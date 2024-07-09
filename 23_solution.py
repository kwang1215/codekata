def solution(x):
    count = 0

    if x == 1:
        count = 0

    while x > 1:
        count += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

    if count > 500:
        count = -1
    return print(count)

solution(1)