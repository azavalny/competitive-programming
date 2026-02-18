class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        goal: min recolorings of white to get k consecutive black blocks
            count frequency of white blocks in current window 
                ^ to do inner loop in O(1) instead of O(n):
                    before incrementing i and after updating curmin, decrement whitecount if i-k was "W"

        W B W B B B W k =2
        ___
          ___
            ___
              ___
curmin= 0   

        W B B W W B B W B W     k =7
                    i
                      i
                        i
                          i
curmin=

    algorithm:
    from k-1 to len(blocks):
        increment whitecount if blocks[i] is white
        decrement whitecount if blocks[i-k+1] was white
        update curmin if smaller whitecount found
        """
        whitecount = sum([1 for c in blocks[:k] if c == "W"])
        curMin = whitecount

        for i in range(k-1+1, len(blocks)):
            if blocks[i] == "W":
                whitecount +=1
            if blocks[i-k] == "W":
                whitecount -=1
            curMin = min(curMin, whitecount)
        return curMin
            