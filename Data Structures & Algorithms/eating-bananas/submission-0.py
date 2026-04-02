import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)

        while (minK <= maxK) :
            mid = minK + maxK
            mid = mid//2
            
            #calculate H
            totalH = 0
            for p in piles:
                totalH += (math.ceil(p/mid))
            if(totalH > h):
                minK = mid + 1
            else:
                maxK = mid - 1
        print(minK, maxK)

        return minK
