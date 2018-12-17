# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Note the description of the problem, if we have `null` in 
        # middle of the input,  this tree is not a complete tree.

        queue = [root]
        
        has_empty = False
                
        while len(queue):
            # get the front of queue and remove it
            node = queue.pop(0)
			
            # if node is empty, flag it
            if node is None:
                has_empty = True
                continue

            # if node is not empty and the tree has empty element
            elif has_empty:
                return False
                
            # visit empty node too
            queue.append(node.left)
            queue.append(node.right)

        return True
