class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas amounts in circular array
        costs of travel to ith to i+1 station

        can we travel from any gas station back to original gas station loop?

        cost: [3,4,5,1,2]
        gas:  [1,2,3,4,5]
                 r
tank: 8
tank = tank value - cost + gas station

g    [2, 2, 4]
c    [1, 2, 3]

start with lowest cost (break ties by largest gas)

minCostIndex
cost[i] vs cost[minCostIndex]
    tie breaker gas[i] vs gas[minCostIndex]
while we havent reached back to minCostIndex:
    tank = tank value - cost + gas station

gas  = [6, 1, 6, 3]
cost = [5, 1, 5, 5]
        """
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0, 0
        for i in range(len(gas)):
            if fuel + gas[i] - cost[i] < 0:
                # can't reach next station:
                # try starting from next station
                start, fuel = i + 1, 0
            else:
                # can reach next station:
                # update remaining fuel
                fuel += gas[i] - cost[i]
        
        return start