class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        operate on triplets any number of times:
            pick 2 triplets and second becomes elementwise max of first and second elemenents
        one of the triplets should have target
        
        1. each element in target must exist somewhere in triplets
        2. pick pairs of triplets with sum closest to but not exceeding target


        [2, 3, 1], [1, 2, 3], [3, 1, 2] target = [2, 2, 2]

        remove triplets with elements larger than target
        then check if each target element exists somewhere in triplets

        [[2,5,3],[2,3,4],[1,2,5],[5,2,3]] target = [5,5,5]
        [[3,5,3],[1,7,5]], target = [3,7,5]
        """
        tripletsCopy = []
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            tripletsCopy.append(t)
        t1Exists = False
        t2Exists = False
        t3Exists = False
        for t in tripletsCopy: 
            if t[0] == target[0]:
                t1Exists = True
            if t[1] == target[1]:
                t2Exists = True
            if t[2] == target[2]:
                t3Exists = True
        return t1Exists and t2Exists and t3Exists