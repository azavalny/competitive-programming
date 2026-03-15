from collections import Counter

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def dist2(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        dists = [
            dist2(p1, p2),
            dist2(p1, p3),
            dist2(p1, p4),
            dist2(p2, p3),
            dist2(p2, p4),
            dist2(p3, p4),
        ]

        freq = Counter(dists)

        if len(freq) != 2:
            return False

        side = min(freq)
        diag = max(freq)

        return freq[side] == 4 and freq[diag] == 2 and side > 0