# 최소직사각형
def solution(sizes):
    long_size = []
    short_size = []
    for num in sizes:
        a, b = num      # 네모 크기 리스트 각각 a,b에 지정
        if a > b:       # 둘중 큰 애들은 큰 애들끼리 모으고 작은 애들은 작은 애들 끼리 모이게 하기
            long_size.append(a)
            short_size.append(b)
        else:
            long_size.append(b)
            short_size.append(a)
    return max(long_size)*max(short_size)   # 큰 애들중 가장 큰 길이 * 작은 애들중 가장 큰 길이

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))