def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*4, reverse=True)

    return str(int('.'.join(numbers)))

print(solution([6, 10, 2]))