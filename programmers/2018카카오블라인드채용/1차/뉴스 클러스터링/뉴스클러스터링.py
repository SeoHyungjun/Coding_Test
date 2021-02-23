# 2021-02-15 17:10 -> 

import re
import math
def solution(str1, str2):
    
    answer = 0
    arr1 = []
    arr2 = []

    str1 = re.sub('[^a-zA-Z]', ' ', str1).lower()
    str2 = re.sub('[^a-zA-Z]', ' ', str2).lower()

    for i in range(len(str1)-1):
        if ' ' not in str1[i:i+2]:
            arr1.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if ' ' not in str2[i:i+2]:
            arr2.append(str2[i:i+2])
    
    '''
    inter = []
    for i in arr1:
        print(arr1, arr2)
        if i in arr2:
            inter.append(i)
            #arr1.pop(a)
            #arr2.pop(a)
            #del arr1[arr1.index(i)]
            del arr2[arr2.index(i)]

    union = arr1 + arr2 + inter
    print(arr1, arr2, inter, union)

    if len(union) == 0:
        return 65536

    return round( len(inter) / len(union)  * 65536 )
    '''
    str1 = arr1
    str2 = arr2
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)
    print(gyo, hap)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

    '''
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    print(str1, str2)

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
'''
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
#str1 = 	"handshake"
#str2 = "shake hands"
str1 = 'aa1+aa2'
str2 = 'aaaa12'
print(solution(str1, str2))