class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        a, b, c, d are unique

        [2,3,4,6]

        4 ways to flip a and b, c and d
        (2, 6, 3, 4)
        (6, 2, 3, 4)
        (2, 6, 4, 3)
        (6, 2, 4, 3)
        * 2 for having c and d in front of a and b with the above combinations

        = n choose 4 *8

        keep track of products and their frequencies
        6: 1
        8: 1
        12: 2 = 2 choose 2 * 8 = 8
        18: 1
        24: 1

        [1,2,4,5,10]
        2: 1
        4: 1
        5: 1
        8: 1
        10: 2 = 2 choose 2 *8 = 8
        20: 2 = 2 choose 2 * 8 = 8
        50: 1
        """
        prods = defaultdict(int) # product: count
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i]*nums[j]
                prods[prod] +=1
        sol = 0
        for key, value in prods.items():
            if value >= 2:
                sol += math.comb(value, 2)*8
        return sol