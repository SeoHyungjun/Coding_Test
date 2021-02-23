# 리스트


List1 = [] # 빈 리스트 선언

List1 = [0 for n in range(5)] # 0으로 채워진 크기 5인 배열 선언

List1 = [0 for n in range(5)] # 0 ~ 4로 채워진 크기 5인 배열 선언

list1.index(value) # 값을 이용하여 인덱스 리턴

list1.insert(index, value) # 리스트 index 위치에 value 삽입

list1.append(value) # 리스트의 맨 뒤에 value 삽입

list1.sort() # 리스트 오름차순 정렬
list1.sort(reverse=True) # 리스트 내림차순 정렬

list1.reverse() # 리스트 안의 값을 역순으로 정렬

list1.extend([value1, value2]) # 리스트 뒤에 배열 또는 값 추가

list1 = str1.split() # 문자열을 리스트로, split은 기본 공백으로 나눔

str1 = ':'.join(list1) # 리스트의 인자 사이에 :을 넣어서 문자열로 만들기

list1[a:b] # 리스트의 a~b-1 인덱싱

list1[a:b:c] # 리스트의 a~b-1까지 c간격으로 인덱싱

str1 = list(map(str, list1)) # 정수형 리스트를 문자열 리스트로 매핑

strlist1.sort(key = lambda x:x*3, reverse=True) # x*3을 해주면 문자열은 xxx형식으로 늘어나게 됨
#이를 통해 늘어난 문자열을 기준으로 정렬

str(int(''.join(list1))) # 문자열 리스트를 숫자로 바꾼 뒤 (000 -> 0) 오버플로우 피하기위해 문자로 변경

'BB'.rjust(5, 'A') # 문자열 BB가 오른쪽으로 가고 5칸으로 채우는데 빈 공간은 A가 들어감 -> AAABB 형태로 변환
'BB'.ljust(7, 'A') # 문자열 BB가 왼쪽으로 가는데 총 길이는 7이되므로 -> BBAAAAA 형태로 변환

#######################
# 스택 # 후입선출(LIFO)

list1 = [] # 스택 선언

list1.append(1) # 맨 뒤에 새로운 원소 삽입

list1.pop() # 맨 뒤의 원소 제거 및 값 가져오기

list1.top() # 맨 뒤의 원소 값 가져오기만 (삭제 x)

##########################
# 큐 # 선입선출(FIFO)

queue = [4, 5, 6]

queue.append(7) # 맨 뒤에 새로운 원소 삽입

queue.pop(0) # 0번째 인덱스 원소 제거 및 값 가져오기