def stack_example():
    stack = [] #스택을 구현하기 위해 리스트 사용
    stack.append(5) #stack에 5 삽임 (list의 마지막에 값을 추가하는 append()가 stack의 push와 같은 역)
    stack.append(2) #stack에 2 삽임
    stack.append(3) #stack에 3 삽임
    stack.append(6) #stack에 6 삽임
    stack.pop() #stack의 마지막 값을 제거 (list의 마지막 값을 빼는 pop()이 stack의 pop과 같은 역할)
    stack.append(1) #stack에 1 삽임
    stack.append(7) #stack에 7 삽임
    stack.pop() #stack의 마지막 값을 제거

    print("스택 출력 : ", stack)
    print("스택 역순 출력 : ", stack[::-1])

stack_example()