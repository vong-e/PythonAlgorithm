# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for command in commands:
        split = array[command[0] - 1:command[1]]
        split.sort()
        answer.append(split[command[2] - 1])

    print(answer)


solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])