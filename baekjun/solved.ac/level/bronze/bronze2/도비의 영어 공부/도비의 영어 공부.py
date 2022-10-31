import sys

while True:
    user_input = sys.stdin.readline().rstrip()
    if user_input == "#": break
    
    print(user_input[0], user_input[2:].lower().count(user_input[0]))