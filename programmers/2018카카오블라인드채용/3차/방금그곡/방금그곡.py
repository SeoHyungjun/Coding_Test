# 2021-02-26 18:00 -> 18:53

import re

def solution(m, musicinfos):
    answer = ''
    check = 0 

    for music in musicinfos:
        start, end, name, mel = music.split(',')
        start = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        end = int(end.split(':')[0]) * 60 + int(end.split(':')[1])

        mel = list(mel)
        while '#' in mel:
            i = mel.index('#')
            mel[i-1] = mel[i-1].lower()
            del mel[i]
        mel = ''.join(mel)
        melody = ''

        m = list(m)
        while '#' in m:
            i = m.index('#')
            m[i-1] = m[i-1].lower()
            del m[i]
        m = ''.join(m)
        melody = ''

        # 시간에 맞춰 총 재생된 멜로디 분류
        if (end - start) > len(mel):
            melody = mel*((end-start)//len(mel)) + mel[:(end-start)%len(mel)]
        else:
            melody = mel[:end-start]

        print(start, end, name, mel, melody)

        print(m, melody)
        if m in melody:
            
            if check < end-start:
                check = end-start
                answer = name

    
    if answer == '':
        return "(None)"
    return answer


m = 'ABCDEFG'
m = "CC#BCC#BCC#BCC#B"
#m = 'ABC'
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']
#musicinfos = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']
print(solution(m, musicinfos))