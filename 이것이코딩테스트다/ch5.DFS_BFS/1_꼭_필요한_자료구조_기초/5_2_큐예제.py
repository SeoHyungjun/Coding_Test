# queue는 선입선출(FIFO, First In First Out)

# append(data)를 통해 맨 뒤에 데이터 삽입
# popleft()를 통해 맨 왼쪽(첫번째) 데이터 제거
    
# stack과 마찬가지로 리스트로 구현 가능
# 그러나 deque가 데이터를 넣고 빼는 속도가 리스트에 비해 효율적
    # 리스트의 경우 pop(0)을 통해 맨 앞의 데이터 제거 가능
    # 그러나 pop(0)을 할 경우
    # [0][1][2][3].....형태로 존재할 경우
    # 0이 제거되면
    # [Null][1][2][3].... 이되고
    # [1][2][3].....과같이 모든 데이터들을 한칸씩 앞으로 당기는 작업을 수반
    # 즉 O(1)이 아닌 O(n)이 되므로 퍼포먼스 극악....
    # 차라리 뒤집어서 pop을 하는게 빠름....

# list(queue)를 통해 deque 자료형을 리스트로 변경 가능

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)