class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def fibo(num):
            if num not in memo:
                memo[num] = fibo(num-1) + fibo(num-2)
            return memo[num]

        memo = {1: 1, 2: 1}

        # fibo(44) < 10**9 < fibo(45)
        max_num = 45
        fibo(max_num)
        answer = 0
        while k:
            for n in range(max_num, 1, -1):
                if memo[n] > k:
                    continue
                # k -= k//memo[n] * memo[n]
                k -= memo[n]
                max_num = n - 1
                answer += 1

        return answer

print(Solution().findMinFibonacciNumbers(7))
print(Solution().findMinFibonacciNumbers(10))
print(Solution().findMinFibonacciNumbers(19))