s = '{()}'
answer = True
stack = []
reverse = {')':'(', ']':'[', '}':'{'}

for i in range(len(s)):
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
        stack.append(s[i])
        
    elif not stack:
        answer = False
        break
        
    elif stack.pop() != reverse[s[i]]:
        answer = False
        break

print('true' if answer else 'false')
        