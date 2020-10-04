# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    print(answer)


def dfs(numbers, target, result_num, index):
    total = 0
    if index == len(numbers):
        if target == result_num:
            total += 1
        return total
    else:
        return dfs(numbers, target, result_num + numbers[index], index + 1) + \
               dfs(numbers, target, result_num - numbers[index], index + 1)


test_numbers = [1, 1, 1, 1, 1]
test_targer = 3
solution(test_numbers, test_targer)
