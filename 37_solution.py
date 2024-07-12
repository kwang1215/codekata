# 행렬의 덧셈

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

arr3 = [[1], [2]]
arr4 = [[3], [4]]


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr1[i])):
            result.append(arr1[i][j] + arr2[i][j])
        answer.append(result)
    return answer


print(solution(arr1, arr2))
print(solution(arr3, arr4))