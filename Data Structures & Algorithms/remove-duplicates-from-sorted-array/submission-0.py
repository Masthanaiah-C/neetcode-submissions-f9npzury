class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newIndex = 1
        for index in range(1,len(nums)):
            if (nums[index]== nums[index-1]):
                continue
            else:
                nums[newIndex] = nums[index]
                newIndex+=1
        return newIndex