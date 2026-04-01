class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary for Frequency.
        DictK = dict()
        for n in nums:
            if n not in DictK:
                DictK[n] = 1
            else:
                DictK[n] += 1
        
        freqList = DictK.values()
        #print(freqList)
        freqList = (sorted(freqList)[-1::-1])[:k]
        #print(freqList)
        finalIndices = list()
        for key, value in DictK.items():
            if value in freqList:
                finalIndices.append(key)
        
        return finalIndices