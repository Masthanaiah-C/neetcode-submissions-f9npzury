class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set(nums[0:k])
        if(len(myset) < k):
            return True
        for i in range(k,len(nums)):
            
            myset.add(nums[i])    
            if(len(myset) < k+1):
                return True
            myset.remove(nums[i-k])
        return False