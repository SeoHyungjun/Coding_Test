class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        
        arr = [nums[-1]]
        for i in range(length - 2, -1, -1):
            answer[i] = bisect_left(arr, nums[i])
            arr.insert(answer[i], nums[i])
            
        return answer