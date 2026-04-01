class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #initialising variables
        minlen = len(nums) + 1
        left = 0
        right = 0
        sumArray = nums[0]
        # Repeat until the right completes the last index of the array
        while (left <= right):
            print(left, right, sumArray)
            #Check Sum 
            if (sumArray >= target):
                minlen = min(minlen, right - left + 1)
                sumArray -= nums[left]
                left += 1
            # Sum less than target
            else:
                right += 1
                if (right == len(nums)):
                    break
                sumArray += nums[right]
            
        
        if (minlen > len(nums)):
            return 0
        else:
            return minlen



