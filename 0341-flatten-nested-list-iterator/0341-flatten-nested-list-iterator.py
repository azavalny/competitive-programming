# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    """
    each element is integer or list of integers ==> flatten

    lazy next()-ing without flatten first

    [[1,1],2,[1,1]]
    next() 6 times = [1,1,2,1,1]

    [1,[4,[6]]] 
    next() 3 times = [1, 4, 6]

stack = [6 4 1]
    """
    def flatten(self, n: [NestedInteger]):
        if n.isInteger():
            return [n.getInteger()]
        sol = []
        for nestedInt in n.getList():
            sol = sol + self.flatten(nestedInt)
        return sol

        """
        flatten([4,[6]])
            sol = []
                self.flatten(4)
                    return 4
                self.flatten([6])

        """

    def __init__(self, nestedList: [NestedInteger]):
        self.sol = []
        for i, n in enumerate(nestedList):
            if n.isInteger():
                self.sol.append(n.getInteger())
            else:
                self.sol = self.sol + self.flatten(n)
            
    def next(self) -> int:
        if self.hasNext():
            return self.sol.pop(0)
    
    def hasNext(self) -> bool:
        if self.sol:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())