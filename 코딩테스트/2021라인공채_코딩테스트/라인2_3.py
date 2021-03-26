import re
from collections import deque

def solution(program, flag_rules, commands):
    # 정답을 저장할 리스트
    answer = []

    # 찾는데 빠르게하기 위해서 flag_rules 를 딕셔너리로 저장
    dic_flag_rules = {}
    alias = deque()
    # 중복되는 flag rule 딕셔너리 
    check = {}

    for f in flag_rules:
            f = f.split()
            if f[1] == 'ALIAS':
                alias.append((f[0], f[2]))
                check[f[0]] = f[2]
                check[f[2]] = f[0]
            else:
                dic_flag_rules[f[0]] = f[1]
    print(check)

    # 별멍을 추가하기 위한 반복문
    # 별명에 별명이 들어갈 경우 별명이 먼저 추가 안되어있을 수 있어 
    # queue 형태로 맨 뒤로 보내어 나중에 다시 체크
    while alias:
        # 저장된 alias를 받아와 저장해야하는 new와 이미 dic에 저장되어있을 prev로 나눔
        new, prev = alias.popleft()

        # 만약 alias의 alias인데 저장이 아직 안되어 있을 경우
        if prev in dic_flag_rules:
            dic_flag_rules[new] = dic_flag_rules[prev]
        # dic안에 저장되어 있을 경우
        else:
            alias.append((new, prev))
        
        print(dic_flag_rules)

    # commands를 하나씩 반복문으로 실행
    for com in commands:
        # 각 command의 맨 앞은 programname이므로 따로 분리하여 저장
        program_name = com.split()[0]
        
        # 만약 입력된 program 명과 현 command의 program_name이 다를경우 -> False
        if program_name != program:
            state = False

        # 입력된 progam 명이 program_name 과 같을 경우 다른 조건 확인
        else:
            # 시작을 True로 하여, 모든 실패 조건을 하나도 만족하지 않을 경우 True 리턴, 하나라도 만족 못하면 False
            state = True

            # command에서 program_name의 뒷 부분을 flag로 설정
            # 만약 flag에 flag_name('-'를 포함하는 문자)이 없을 경우
            # False
            if '-' not in ' '.join(com.split()[1:]):
                answer.append(False)
                break

            # 있을 경우 flag를 '-'기준으로 나누어 리스트로 저장
            else:
                flags = [a for a in ' '.join(com.split()[1:]).split('-') if a]

            # 나눠진 flag들을 하나씩 반복문으로 실행
            for flag in flags:
                # 각 flag에서 맨 앞은 f_name으로 설정
                f_name = '-'+flag.split()[0]
                # 각 flag에서 맨 앞을 제외한 모든 것들은 f_type으로 설정 (flag_argument_type과 비교되는 대상)
                f_type = flag.split()[1:]

                # f_name이 flag_rules에 없을경우
                if f_name not in dic_flag_rules:
                    state = False
                    break

                # f_name이 있을 경우
                else:
                    if f_name not in dic_flag_rules:
                        state = False
                        break

                    if f_name in check:
                        print(dic_flag_rules)
                        del dic_flag_rules[check[f_name]]
                        del check[check[f_name]]
                        del check[f_name]

                    

                    # flag rule이 stings일 경우 (1개 이상이므로)
                    if dic_flag_rules[f_name] == 'STRINGS':
                        # strings가 적어도 1개 있어야하지만, 아무것도 없으므로 false
                        if not f_type:
                            state = False
                            break
                            
                        # 각 flag에 숫자가 들어갔을 경우 false
                        for ty in f_type:
                            if re.findall('[0-9]', ty):
                                state = False
                                break
                    
                    # flag rule이 string일 경우
                    if dic_flag_rules[f_name] == 'STRING':
                        # flag rule이 string일 경우 1개만 존재해야 하므로 0일때와 2이상일때 false
                        if len(f_type) != 1:
                            state = False
                            break
                        
                        # 만약 숫자가 포함되어있다면 false
                        elif re.findall('[0-9]', f_type[0]):
                            state = False
                            break
                    

                    # flag rule이 Numbers일 경우
                    elif dic_flag_rules[f_name] == 'NUMBERS':
                        # numbers에 적어도 1개 있어야하지만, 아무것도 없으므로 false
                        if not f_type:
                            state = False
                            break

                        # 각 flag에 문자가 들어갔을 경우 flase
                        for ty in f_type:
                            if re.findall('[a-zA-Z]', ty):
                                state = False
                                break
                    
                    # flag rule이 number일 경우
                    if dic_flag_rules[f_name] == 'NUMBER':
                        # flag rule이 numver일 경우 1개만 존재해야 하므로 0일때와 2이상일때 false
                        if len(f_type) > 1:
                            state = False
                            break
                        
                        # flag에 문자가 들어갔을 경우 false
                        elif re.findall('[a-zA-Z]', f_type[0]):
                            state = False
                            break
                    
                    # flag rule이 null일 경우
                    elif dic_flag_rules[f_name] == 'NULL':
                        # flag가 비어있지 않은 경우 false
                        if f_type:
                            state = False
                            break
        answer.append(state)
    return answer

print(solution(	"line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))

# print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
# print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))


# print(solution(	"line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
# print(solution("line", 	["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))

