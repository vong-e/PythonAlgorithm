from _collections import deque #큐 자료구조 사용을 위해 deque라이브러리 사용

def queue_example():
    queue = deque() #큐 선언
    queue.append(7) #큐에 (7)삽입
    queue.append(5) #큐에 (5)삽입
    queue.append(2) #큐에 (2)삽입
    queue.popleft() #삭제 -> (7)삭제 (큐에서는 가장 먼저 들어온 원소가 먼저 삭제됨, 선입선출)
    queue.append(1) #큐에 (1)삽입
    queue.append(6) #큐에 (6)삽입
    queue.popleft() #삭제 -> (5)삭제

    print("큐 출력: ",queue)
    queue.reverse()
    print("큐 역순 출력", queue)

queue_example()