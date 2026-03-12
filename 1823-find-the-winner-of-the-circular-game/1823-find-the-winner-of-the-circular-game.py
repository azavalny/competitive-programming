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
        """
        friends = [i + 1 for i in range(n)]
        friends_killed = 0
        starting_index = 0

        while friends_killed != n - 1:
            new_index = starting_index % n
            steps = 0

            while friends[new_index] == 0 or steps < k - 1:
                if friends[new_index] != 0:
                    steps += 1
                new_index = (new_index + 1) % n

            friends[new_index] = 0
            friends_killed += 1
            starting_index = (new_index + 1) % n

        return sum(friends)