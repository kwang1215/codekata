# 내적
def solution(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return sum(result)

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))