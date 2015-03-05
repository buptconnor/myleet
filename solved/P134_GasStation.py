__author__ = 'Connor'

# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        res = [gas[i] - cost[i] for i in range(N)]
        i = 0
        while i < N:
            if res[i] < 0:
                i += 1
                continue
            can = True
            cur = 0
            j = 0
            while j < N:
                cur += res[(j + i) % N]
                if cur < 0:
                    can = False
                    break
                j += 1
            if can == False:
                i += (j+1)
                continue
            else:
                return i
        return -1





