class Solution:



     def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = dict()
        prefixList = [0]
        totalSum = 0
        for n in nums:
            prefixList.append(prefixList[-1] + n)
        #print(prefixList)
        prefixSum[0] = 1
        for n in prefixList[1:]:
            if((n-k)  in prefixSum.keys()):
                #print(n,k)
                totalSum = totalSum + prefixSum[n-k]
            #print(prefixSum)
            if n not in prefixSum.keys():
                prefixSum[n] = 1
            else:
                prefixSum[n] = prefixSum[n] + 1
            
        #print(prefixSum)
        return totalSum

