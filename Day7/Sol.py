# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def check(root,last,depth,x,y):
            if not root:
                return
            if root.val==x:
                Solution.xdepth=depth
                Solution.xlast=last
                return 
            if root.val==y:
                Solution.ydepth=depth
                Solution.ylast=last
                return
            check(root.left,root,depth+1,x,y)
            check(root.right,root,depth+1,x,y)
        
        Solution.xdepth=0
        Solution.ydepth=0
        Solution.xlast=None
        Solution.ylast=None
        
        check(root,root,1,x,y)
        if Solution.xdepth==Solution.ydepth and Solution.xlast!=Solution.ylast:
            return 1
        else:
            return 0
        
        
        