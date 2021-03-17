# 2021-03-10 17:41 -> 17:45

def solution(nums):
    select_num = len(nums)//2

    if select_num >= len(set(nums)):
        return len(set(nums))

    return select_num



nums = [3,1,2,3]
print(solution(nums))