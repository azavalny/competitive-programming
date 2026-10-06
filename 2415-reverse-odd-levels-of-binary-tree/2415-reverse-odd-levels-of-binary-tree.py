# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        """
        perfect binary tree = 2 children for every parent + all leaves on same level

        reverse node values at each odd level of tree and return root of the reversed tree

         up to 2^14 nodes

        use BFS to reconstruct odd levels into new tree and maintain levels as counter
        
        use BFS + maintain queue of even levels and swap their children (odd levels)
            left_node = current.left
            left_left_child
            left_right_child 

            right_node
            right_left_node
            right_right_node

            left_node.left = right_left_node
            left_node.right = right_right_node

            right_node.left = left_left_node
            right_node.right = left_right_node
        ^ dosent work
        
        CHILDREN NODES SHOULD REMAIN THE SAME SO JUST RENAME THE VALUES

        BFS queue for each level:
            on odd levels, make copy of queue and reset values
        """
        queue = deque([root])
        level=0
        while queue:
            if level%2!=0:
                reversed_vals = list(reversed([node.val for node in queue]))
                for i in range(len(queue)):
                    current = queue[i]
                    current.val = reversed_vals[i]
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level +=1
        return root