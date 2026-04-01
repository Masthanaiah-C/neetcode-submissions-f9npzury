class Solution:
    def swapNums (self, nums, i, j):
        num = nums[i]
        nums[i] = nums[j]
        nums[j] = num
        return
    def sortColors(self, nums: List[int]) -> None:
        #bruteforce 
        #sort the array - O(nlog(n)) complexity

        #map 
        #find how many 1s, 1s and 2s and then overwrite the array in second pass
        # 2 passes. 
        
        #1 pass solution
        index = 0
        n = len(nums)  
        twoIndex = n - 1
        zeroIndex = 0

        while (index < n and index <= twoIndex):
            if(nums[index] == 2):
                self.swapNums(nums, index, twoIndex)
                twoIndex -= 1
                continue
            if (nums[index] == 0):
                self.swapNums(nums, index, zeroIndex)
                zeroIndex +=1
                if(index < zeroIndex):
                    index+=1
                continue
            if(nums[index] == 1 ):
                index+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        