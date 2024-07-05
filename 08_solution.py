def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle <180:
        answer = 3
    elif angle == 180:
        answer = 4
    return print(answer)

solution(70)
solution(91)
solution(180)

