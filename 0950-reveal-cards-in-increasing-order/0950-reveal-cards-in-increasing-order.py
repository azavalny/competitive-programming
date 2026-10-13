class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """
        return ordering of revealed cards in increasing order

        can sort in order of pairs where first cards increasing order

        [17,13,11,2,3,5,7] => [2,13,   3,11,   5,17,    7]

    while unrevealed cards:
        reveal top card and remove
        next top card at back of deck


        even indicies we give first half of sorted values
        for each 2nd value:
            skip
            put next largest value

        [2, 3, 5, 6, 7, 11, 13, 17]
        Queue of solution indicies
        

        """
        deck.sort()
        q = deque(range(len(deck)))
        sol = [0]*len(deck)

        for n in deck:
            i = q.popleft()
            sol[i] = n
            if q:
                q.append(q.popleft())
        return sol