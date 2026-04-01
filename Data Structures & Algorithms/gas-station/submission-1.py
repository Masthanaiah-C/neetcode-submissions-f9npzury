class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        net = list()
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            net.append(gas[i] - cost[i])
        print (net)
        if (total < 0):
            return -1
        else:
            index = 0
            sumn = 0
            for n in range(len(net)):
                sumn += net[n]
                if (sumn < 0):
                    index = n+1
                    sumn = 0
            return index