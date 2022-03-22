import sys

def change_text(t, k):
    if t == ' ':
        return ' '
    
    changed_t = ord(t) - (ord(k) - ord('a') + 1)
    if ord('a') > changed_t:
        changed_t += ord('z') - ord('a') + 1
    return chr(changed_t)

text = sys.stdin.readline().rstrip()
crypt_key = sys.stdin.readline().rstrip()
answer = ''
key_index = 0

for t in text:
    answer += change_text(t, crypt_key[key_index])
    key_index = (key_index + 1) % len(crypt_key)

print(answer)