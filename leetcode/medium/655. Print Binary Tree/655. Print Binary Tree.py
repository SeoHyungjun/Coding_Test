# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        tree = {}
        
        max_depth = 0
        queue = deque()
        queue.append((1, 0, root))
        while queue:
            idx, depth, cur = queue.popleft()
            tree[idx] = cur.val
            max_depth = max(max_depth, depth)

            if cur.left:
                    queue.append((2*idx, depth+1, cur.left))
            if cur.right:
                    queue.append((2*idx + 1, depth+1, cur.right))
                    
        answer = [[""] * (2**(max_depth+1) - 1) for _ in range(max_depth+1)]
        
        queue.append((0, (2**(max_depth+1) - 1)//2, root))
        while queue:
            row, col, cur = queue.popleft()
            answer[row][col] = str(cur.val)
            
            if cur.left:
                queue.append((row+1, col-2**(max_depth-row-1), cur.left))
            if cur.right:
                queue.append((row+1, col+2**(max_depth-row-1), cur.right))
        
        return answer