"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {e.id : e for e in employees}
        
        answer = 0
        queue = deque([id])
        while queue:
            cur = dic[queue.popleft()]
            answer += cur.importance
            
            for child in cur.subordinates:
                queue.append(child)
                
        return answer
            
            