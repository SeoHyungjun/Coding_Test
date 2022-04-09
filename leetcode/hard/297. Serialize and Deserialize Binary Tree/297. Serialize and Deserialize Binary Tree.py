# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        
        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def maker(nodes):
            if not nodes or (cur_val:=nodes.popleft()) == 'null':
                return None
            
            root = TreeNode(cur_val)
            root.left = maker(nodes)
            root.right = maker(nodes)
            
            return root
        
        return maker(deque(data.split()))
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))