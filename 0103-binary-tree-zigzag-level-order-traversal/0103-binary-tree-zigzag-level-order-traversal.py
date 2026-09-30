# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        while nodes in queue:
            for each children at current length of queue:
                add its neighbors to queue but in reverse if odd, otherwise normally
            flip levelSign
        """
        if not root:
            return []
        queue = deque([root])
        sol = []
        level=0
        while queue:
            current_level = []
            for i in range(len(queue)):
                child = queue.popleft()
                current_level.append(child.val)
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)

            if level%2 !=0:
                current_level.reverse()

            sol.append(current_level)
            level+=1
        return sol