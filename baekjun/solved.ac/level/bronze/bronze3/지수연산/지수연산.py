import sys

N = int(sys.stdin.readline())
changed = "%.300f"%(2**-N)

for i in range(len(changed) - 1, -1, -1):
    if changed[i] == '0':
        continue
        
    print(changed[:i+1])
    break