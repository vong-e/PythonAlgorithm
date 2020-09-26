# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for scov in scoville:
        heapq.heappush(heap, scov)

    while heap[0] < K:
        if len(heap) < 2: #음식을 섞으면서 힙(음)의 갯수가 2보다 작아졌을떄식(음식이 하나만 남음) -> 더이상 섞을 수 없음
            if heap[0] < K: #남은 음식이 K보다 작을 때 -> K보다 높게 만들 수 없음.
                return -1
            break

        first_min = heap[0]
        heapq.heappop(heap)
        second_min = heap[0]
        heapq.heappop(heap)
        heapq.heappush(heap, mixFood(food1=first_min, food2=second_min))
        print("이떄 힙: ",heap)
        answer += 1

    return answer

def mixFood(food1, food2):
    print(f"food1: {food1}, food2: {food2}")
    return food1 + food2*2

input_scoville = [1, 2, 3, 9, 10, 12]
input_K = 7
print("테스트 케이스: ", solution(scoville=input_scoville, K=input_K))
