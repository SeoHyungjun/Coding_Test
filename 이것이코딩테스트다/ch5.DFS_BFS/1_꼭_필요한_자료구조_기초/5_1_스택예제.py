# stack은 후입선출(LIFO, Last In First Out)

# 파이썬에서는 list를 사용하여 stack처럼 사용 가능
# stack.append(data) -> 맨 뒤에 데이터 삽입
# stack.pop() -> 맨 뒤의 데이터 제거 및 가져오기
    
    # pop(index)를 통해 원하는 위치의 데이터 제거가능
    # stack.pop(0) -> stack의 0번째(맨앞)의 데이터 pop
    
    # pop()의 경우 stack에서 데이터를 제거하고, 해당 데이터를 return
    # a = stack.pop()

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
