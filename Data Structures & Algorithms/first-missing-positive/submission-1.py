class Solution:
    def swapPosition(self, nums: List[int], i: int , j: int) -> None:
        num = nums[i]
        nums[i] = nums[j]
        nums[j] = num
        return None
        
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Discard all the negative numbers
        count = len(nums)
        prevSwap = 1
        for i in range(count):
           while(prevSwap != nums[i]):
            prevSwap = nums[i]
            if ((nums[i] <= count) and (nums[i] > 0) and (nums[i] != i+1)):
                self.swapPosition(nums, i, nums[i] - 1)
                
                #print(nums)
        for i in range(count):
            if (nums[i] != i+1):
                return i+1

        return count+1