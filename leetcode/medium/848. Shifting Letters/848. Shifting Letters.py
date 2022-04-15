# Runtime : 768
# faster than 99.55%

import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
        alpha = list(string.ascii_lowercase)
        length = len(alpha)
        
        answer = list(s)
        move_sum = 0
        
        for i in range(len(shifts)-1, -1, -1):
            move_sum += shifts[i]
            answer[i] = alpha[(ord(answer[i]) - ord('a') + move_sum) % length]

        return ''.join(answer)