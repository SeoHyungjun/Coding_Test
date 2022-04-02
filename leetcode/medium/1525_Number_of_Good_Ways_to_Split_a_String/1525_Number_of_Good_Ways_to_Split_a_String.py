class Solution:
    def numSplits(self, s: str) -> int:
        answer = 0
        left = set()
        right = set(s)
        
        alpha = [0] * 26
        for w in s:
            alpha[ord(w) - ord('a')] += 1
            
        for i in range(len(s) - 1):
            left.add(s[i])
            
            alpha[ord(s[i]) - ord('a')] -= 1
            if alpha[ord(s[i]) - ord('a')] == 0:
                right.remove(s[i])

            if len(left) == len(right):
                answer += 1

        return answer