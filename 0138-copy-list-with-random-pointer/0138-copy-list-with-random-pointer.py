"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        return deep copy of the linked list given head
        None of the pointers in the new list should point to nodes in the original list

        Node: [value, random_index] + next_node
        random_index = index of another node [0, n-1]

        O(n^2)
        for each node
            create a copy with same value
            set previous.next to current
            set random to previous node so we can loop backwards later
        construct array representing indexes of each node
        in 2nd pass, for each copied node
            find the node pointed to by random by looping forward/backward and then set random to that Node

        O(n)
        1st paass
            build hashmap of oldNode : newNode(value)
        in 2nd pass for each original
            new_node = map[original]
            new_node.next = map[original.next]
            new_node.random = map[original.random]
        return map[original's head]
        {
            7 : new 7, next= new 13, random= new null
            13: new 13, next= new 11, r= new 7
            11 : new 11, next= new 10, r= new 1
            10 : new 10, next= new 1, random= new 11
            1: new 1, next= new null, random = new 7
            null : new null, next=None, random = None
        }
        """
        if not head:
            return None

        builder_map = {}
        
        curr = head
        while curr != None:
            builder_map[curr] = Node(curr.val)
            curr = curr.next
        for original in builder_map.keys():
            if original.next:
                builder_map[original].next = builder_map[original.next]
            else:
                builder_map[original].next = None
            if original.random:
                builder_map[original].random = builder_map[original.random]
            else:
                builder_map[original].random = None
        return builder_map[head]