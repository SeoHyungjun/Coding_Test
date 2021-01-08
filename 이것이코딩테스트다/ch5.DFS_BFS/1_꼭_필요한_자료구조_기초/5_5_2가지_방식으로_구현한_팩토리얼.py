# 실행 결과는 동일
# 재귀 함수의 코드가 더 간결 -> 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문

# n이 0 또는 1일때 factirial(n) = 1이므로 종료조건
# 팩토리얼은 n이 양의 정수일 때만 유효
# n이 음수가 들어오면 입력 범위 오류
# n이 1 이하인 경우를 고려하지 않으면(종료 조건을 설정하지 않으면) 재귀 함수가 무한히 반복



# 반복문으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i

    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1
    
    # n! = n * (n-1)!를 그대로 코드로 작성
    return n * factorial_recursive(n-1)


# 각각의 방식으로 구현한 n! 출력 (n = 5)
print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
