# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
    # recursive method, DFS, 40%
        if not(root):   return []
        result = []
        self.tracker(root, '', result)
        return result
        
    def tracker(self, node, path, result):
        if not(node.left) and not(node.right):
            result.append(path+str(node.val))
        if node.left:
            self.tracker(node.left, path+str(node.val)+"->", result)
        if node.right:
            self.tracker(node.right, path+str(node.val)+"->", result)
    '''    
    # iterative method, BFS, 45%
    def binaryTreePaths(self, root):
        if not root:    return []
        result = []
        stack = [(root, "")]    #(node, path) tuples
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path+str(node.val))
            if node.left:
                stack.append((node.left, path+str(node.val)+"->"))
            if node.right:
                stack.append((node.right, path+str(node.val)+"->"))
        return result   
    '''
   