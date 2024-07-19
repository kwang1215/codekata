# 시저 암호
import string


def solution(s, n):
    str_alphabet = string.ascii_lowercase
    answer = ''
    for word in s:
        if word.isalpha():  # 문자가 알파벳인지 확인
            # 소문자 처리
            if word.islower():
                new_index = (str_alphabet.index(word) + n) % 26
                answer += str_alphabet[new_index]
            # 대문자 처리
            else:
                new_index = (str_alphabet.index(word.lower()) + n) % 26
                answer += str_alphabet[new_index].upper()
        else:
            # 알파벳이 아닌 문자는 그대로 추가
            answer += word
    return answer


print(solution("AB", 1))
print(solution("z",1))
print(solution("a B z", 4))