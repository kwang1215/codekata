# 삼총사
def triple_stu(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    count += 1
    return count


numbers = [-2, 3, 0, 2, -5]
numbers = [-3, -2, -1, 0, 1, 2, 3]
numbers = [-1, 1, -1, 1]
print(triple_stu(numbers))