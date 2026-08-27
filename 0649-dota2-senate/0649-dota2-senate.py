class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        R, D party
        for each senator
            in each round:
                senator can pick another senator to skip for rest fo round
                if current senator found another group of same senators, he wins round and decide on change
        
        best strategy, each person eliminates max # of people from each party
        RDDR

        frequency of R's vs D's

        RDDR - R ends D, D ends first R, R remains

        RDDRD

        D [4, 7(2)] 
           i
        R [5(0)]
           j
        make 2 deques
        loop over senate and push each index to corresponding deque
        begin looping while both are nonempty:
            choose smaller index of the front of both deques and push to end (account for if the length of the deque has been reached to cycle)
            choose larger index of and remove

        RRRRDD
        """
        d = deque([])
        r = deque([])
        for i, s in enumerate(senate):
            if s == "D":
                d.append(i)
            else:
                r.append(i)
        while len(d) > 0 and len(r) > 0:
            dI = d.popleft()
            rI = r.popleft()
            if dI < rI:
                d.append(dI + len(senate))
            else:
                r.append(rI + len(senate))
        if len(d) > 0:
            return "Dire"
        else:
            return "Radiant"