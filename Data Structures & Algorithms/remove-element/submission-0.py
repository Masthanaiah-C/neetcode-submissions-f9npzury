class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index2Place = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[index2Place] = nums[i]
                index2Place += 1
        return index2Place