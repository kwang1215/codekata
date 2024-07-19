# 숫자 문자열과 영단어
def solution(s):
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    for word, num in number_dict.items():
        s = s.replace(word, str(num))
    return int(s)


print(solution("23four5six7"))
