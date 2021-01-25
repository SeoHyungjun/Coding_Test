array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result)

array = [('바나나', 3), ('바나나', 2), ('사과', 5), ('사과', 1), ('사과', 9), ('당근', 3)]


result = sorted(array, key = lambda x: (x[1], x[0]))
print(result)