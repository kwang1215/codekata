def solution(seoul):
    for i, person in enumerate(seoul):
        if "Kim" in person:
            answer = f'김서방은 {i}에 있다'
    return answer

