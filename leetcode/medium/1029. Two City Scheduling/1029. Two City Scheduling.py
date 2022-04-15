# Runtime : 40ms
# faster than : 92.60%

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:(x[0] - x[1]))
        
        answer = 0
        N = len(costs)
        for i in range(N//2):
            answer += costs[i][0]
            
        for i in range(N//2, N):
            answer += costs[i][1]
            
        return answer