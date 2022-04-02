class Solution:
    def findMinDifference(self, timePoints): #: List[str]) -> int:
        minutes = sorted([int(time[:2])*60 + int(time[3:]) for time in timePoints])

        answer = 1440 + minutes[0] - minutes[-1] # 1440m = 24h * 60m
        for i in range(len(minutes)-1):
            answer = min(answer, minutes[i+1] - minutes[i])

        return answer


print(Solution().findMinDifference(["23:59","00:00"]))