
def a(num, zin):
    result = ''
    hex_arr = '0123456789ABCDEF'
    while num > 0:
        num, mod = divmod(num, zin)
        result += str(hex_arr[mod])

    return result[::-1]

aa = a(100, 15)
print(aa)
print(int(aa, base=15))