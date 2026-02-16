class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        for each item:
            special discount = next smallest or equal element right of current item

        Naive O(n^2):
            nested pointers
        
        Idea 1: use increasing stack and pop if violation occurs and store current price - violated value in index

        Hari:
        DISCOUNT = next smaller or EQUAL element
        goal:
            
            answers[i] =   (current price -  next smaller or EQUAL element from each index)
            increasing stack
            for this example: [1,1]: this company is gonna go broke


        [8, 4, 6, 2, 3]
                     i
stack:  []
answer: [4, 2, 4, 2, 3]
        """
        stack = []
        sol = prices

        for i, p in enumerate(prices):
            while stack and stack[-1][1] >= p:
                discount = p
                older = stack[-1][1]
                index_older = stack[-1][0]
                stack.pop()

                sol[index_older]  = older - discount

            stack.append((i, p))
        return sol