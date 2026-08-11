class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        abab | cc


        ababcbacadefegdehijhklij

        ababcbaca defegde hijhklij
        """
        ends = {}

        # ends of interval
        for i, c in enumerate(s):
            ends[c] = i

        count = 0
        res = []
        end = 0
        for i, c in enumerate(s):
            count +=1
            end = max(ends[c], end)
            if end == i:
                res.append(count)
                count = 0
                end = i + 1
        return res