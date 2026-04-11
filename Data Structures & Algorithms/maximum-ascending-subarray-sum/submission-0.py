class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        Msum = 0

        if (len(nums) == 0):
            return 0
        
        globalSum = nums[0]
        Msum = max(Msum, globalSum)

        for i in range(1,len(nums)):
            if (nums[i] > nums[i-1]):
                globalSum += nums[i]
            else:
                globalSum = nums[i]
            Msum = max(Msum, globalSum)

        return Msum