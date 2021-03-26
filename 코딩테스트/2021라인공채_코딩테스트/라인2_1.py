import re

def solution(program, flag_rules, commands):
    # 정답을 저장할 리스트
    answer = []

    # 찾는데 빠르게하기 위해서 flag_rules 를 딕셔너리로 저장
    dic_flag_rules = {}
    for f in flag_rules:
        argument, type = f.split()
        dic_flag_rules[argument] = type

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


#print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
#print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))


print(solution(	"line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
print(solution("line", 	["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))