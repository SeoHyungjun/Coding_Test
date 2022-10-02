class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def manachers(s):
            ans = [1] * n
            a = [0] * n
            center = right = 0
            for i in range(n):
                if i < right: a[i] = min(right - i, a[2*center - i])
                while 0 <= i-1-a[i] and i+1+a[i] < n and s[i-1-a[i]] == s[i+1+a[i]]:
                    a[i] += 1
                    ans[i+a[i]] = max(ans[i+a[i]], 2*a[i] + 1)
                if right < i+a[i]: center, right = i, i+a[i]
            for i in range(1, n): ans[i] = max(ans[i-1], ans[i])
            return ans
        
        prefix = manachers(s)
        suffix = manachers(s[::-1])
        print(prefix)
        print(suffix)
        print( [(i, ~i) for i in range(1, n)])
        return max(prefix[i-1]*suffix[~i] for i in range(1, n))


#print(Solution().maxProduct("ababbb"))
#print(Solution().maxProduct("zaaaxbbby"))
print(Solution().maxProduct("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"))


"""
string s -> index 0 ~ length-1

0 < = i <= j <= k <= l < length
s[i:j+1] * s[k:l]

dp???

arr = [0 1 2 3 4 5 6 7 8 9]
"""