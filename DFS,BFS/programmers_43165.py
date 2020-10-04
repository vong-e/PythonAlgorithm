# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    print(answer)


def dfs(numbers, target, result_num, index):
    if index == len(numbers):
        # if target == result_num:
        #     return
        print("1")
        return target == result_num
    else:
        return dfs(numbers, target, result_num + numbers[index], index + 1) + \
               dfs(numbers, target, result_num - numbers[index], index + 1)

test_numbers = [1, 1, 1, 1, 1]
test_targer = 3
solution(test_numbers, test_targer)

#
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)