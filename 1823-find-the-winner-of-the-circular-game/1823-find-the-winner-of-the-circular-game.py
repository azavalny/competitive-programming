class Node:
    def __init__(self, val, prevNode=None, nextNode=None):
        self.val = val
        self.prevNode = prevNode
        self.nextNode = nextNode
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        clockwise order N, E, S, W

         rules of the game = simulation problem
         
         state = list of friends in order making dead friend 0
            Doubly Linked List in O(1) removal from middle
            or list because n is small
         remaining friends
         game:
            count next k friends including current wrapping around circle
            last friend counted leaves circle
            if friends remain in circle:
                start from next friend forward (not counting zeros) and repeat
            else:
                last friend remaining wins

            friends = [0, 0, 3, 0, 0], k=2
curFriendIndex               i
friendsRemaining = 1

index: 4 to 0 = (4 + 1)%5

    (index + k-1)%n
    deciding start point at end of loop

    when finding next valid friend you have to keep checking clockwise to find nonzero friend

    ^ this is quadratic time
    to get linear could we use queue by popping when friend dies so no inner while loops


    [1, 0, 0, 0, 0] k = 2
     i

    n = 2 to 5, k = 2
    f(1) = 0
    f(2) = (f(1) + 2)%2 = 0
    f(3) = (f(2) + 2)%3 = 2
    f(4) = (f(3) + 2)%4 = 0

    Linked List:

    [3], k=2
        i
    build doubly linked list
        create head (1)
        from 2 to n:
            create new node
            set new node.prev = prev
            set prev.next = current

            prev = current
        head.prev = current
        current.next = head

        1 <-> 2 <-> 3 <-> 4 <-> 5

    current initially head
     while friends_alive > 1:
        move k-1 nodes
        remove current node and set current to next and next to previous
        friends_alive -=1
    return current.val
        """

        head = Node(1, None, None)
        prev = head
        for i in range(2, n+1):
            newNode = Node(i, prev, None)
            prev.nextNode = newNode

            prev = newNode
        head.prevNode = prev
        prev.nextNode = head
        
        curNode = head
        friendsAlive = n
        while friendsAlive > 2:
            for i in range(k-1):
                curNode = curNode.nextNode
            # removing curNode's pointers
            nextNodeAfter = curNode.nextNode # get next node
            nextNodeAfter.prevNode = curNode.prevNode # set next node's previous to be previous node from current
            prevNode = curNode.prevNode # get previous node
            prevNode.nextNode = nextNodeAfter # set previous node's next to te the next node
            
            curNode = nextNodeAfter # move current node to next and restart

            friendsAlive -=1
        print(curNode.val, curNode.nextNode.val)
        if k%2 == 0:
            return curNode.val
        return curNode.nextNode.val