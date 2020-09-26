#문제: https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    print("prices", prices)
    answer = [0] * len(prices)
    
    for index in range(0, len(prices) - 1):
        print('인덱스는: ',index)
        for j in range(index, len(prices) - 1):
            if prices[index] <= prices[j]:
                print('{}이 {} 보다 작거나같음'.format(prices[index], prices[j]))
                answer[index] += 1
            else:
                break     
        print("====")

    print("이떄 앤써", answer)
    return answer


p = [1, 2, 3, 2, 3]
print("테스트 케이스: ", solution(prices=p))