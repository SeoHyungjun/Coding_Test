# 이 코드를 실행하면
# RecursionError: maximum recursion depth exceeded while calling a Python object 에러가 발생
# 재귀의 최대 깊이를 초과했다는 내용

# 보통 파이썬 인터프리터는 호출 횟수 제한이 있는데, 이 한계를 벗어났기 때문
# 즉, 무한대로 재귀호출을 진행할 수 없음...

def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()

recursive_function()