class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if(len(nums)==0):
            return 0
        count = 1
        maxcount = 1
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                continue
            if (nums[i] - nums[i-1] == 1):
                count += 1
            else:
                count = 1
            maxcount = max(maxcount,count)
        return maxcount


