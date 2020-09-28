def stack_example():
    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.pop()
    stack.append(1)

    print("스택 출력 : ", stack)
    print("스택 역순 출력 : ", stack[::-1])

stack_example()