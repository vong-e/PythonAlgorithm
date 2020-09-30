# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq #힙 자료구조를 사용하기 위해 import

def solution(scoville, K):
    answer = 0
    heap = []

    for scov in scoville:
        heapq.heappush(heap, scov) #scovile배열을 heap 배열에 힙 푸쉬, 기본적으로 min heap됨 으로 정렬

    while heap[0] < K: #heap의 0번쨰 인덱스 즉 min heap이 K보다 크거나 같아질 떄 까지 반복
        if len(heap) < 2: #음식을 섞으면서 힙(음)의 갯수가 2보다 작아졌을떄식(음식이 하나만 남음) -> 더이상 섞을 수 없음
            if heap[0] < K: #남은 음식이 K보다 작을 때 -> K보다 높게 만들 수 없음 -> -1 리
                return -1
            break

        first_min = heap[0] #min heap에서는 0번째 인덱스가 가장 작은 원소임, 그렇다고 1, 2번쨰 인덱스가 두번쨰, 세번째로 작은것은 보장하지 않음
        heapq.heappop(heap) #두번쨰로 작은 원소를 얻기 위해 0번째 인덱스를 pop
        second_min = heap[0] #두번쨰로 작은 원소를 저장
        heapq.heappop(heap) #두번쨰로 작은 원소 pop
        heapq.heappush(heap, mixFood(food1=first_min, food2=second_min)) #위에서 저장한 가장 낮은 scovile을 가진 음식과 두번째로 scovile이 낮은 음식을 섞어서 나온 음식의 scovile을 push
        print("이떄 힙: ",heap)
        answer += 1 #음식을 한 번 섞었으므로 섞은 횟수 1회 증가

    return answer

def mixFood(food1, food2): #턴두 음식을 섞어서 나오는 스코빌 지수를 리턴    print(f"food1: {food1}, food2: {food2}")
    return food1 + food2*2

input_scoville = [1, 2, 3, 9, 10, 12]
input_K = 7

print("테스트 케이스: ", solution(scoville=input_scoville, K=input_K))
