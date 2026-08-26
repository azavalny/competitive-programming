class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        can you rearrange cards to form n groupSize groups of consecutive cards


valid:  [6, 5, 4, | 3, 2, 1], groupsize=3
        

        [1, 2, 3, 6, 2, 3, 4, 7, 8]
                     r
                  l

        must have len(hand)%groupSize == 0 groups
groupcount
        move right pointer until end:
            if you reach non-consecutive element:
                if groupSize was reached:
                    increment groupcount
                    move left pointer to (r-l+1-groupSize)
                else
                
        kadane's algorithm?
        monotonic stack?
        frequency hash table approach

        [1,2,3,6,2,3,4,7,8]


must have len(hand)%groupSize == 0 groups
build frequency counter Counter() and sorted hands
total, startingValue

loop len(hand)%groupSize times:
    loop over consecutive groupSize elements in hash table
        if consecutive element dosent exist return False
        otherwise increment starting
    find next Starting in sorted array
return True

total:
starting: 2
1:0
2:0
3:0
4:0
6:1
7:1
8:1

sorted [1, 2,  2,  3, 3, 4, 6,  7, 8]
                            i
        """
        if len(hand)%groupSize != 0:
            return False
        freq = Counter(hand)
        nextStartingArray = sorted(hand)
        startingIndex = 0

        numGroups = len(hand)//groupSize
        for g in range(numGroups):
            curNextValue = nextStartingArray[startingIndex]
            for i in range(curNextValue, curNextValue + groupSize):
                if i not in freq:
                    return False
                freq[i] -=1
                if freq[i] == 0:
                    del freq[i]
            # finding next starting index
            currentMinValue = nextStartingArray[startingIndex]
            while freq[currentMinValue] == 0 and startingIndex < len(hand):
                startingIndex +=1
                currentMinValue = nextStartingArray[startingIndex] if startingIndex < len(hand) else currentMinValue
        return True