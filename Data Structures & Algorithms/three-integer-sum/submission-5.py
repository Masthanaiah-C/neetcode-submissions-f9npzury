class Solution:
    def checkSum(self, nums, i, j, k):
        if (i<0 or k>=len(nums)):
            return 
        if (nums[i] + nums[j] + nums[k] == 0):
            if ([nums[i] , nums[j] , nums[k]] not in self.finalList):
                self.finalList.append([nums[i] , nums[j] , nums[k]])
            self.checkSum(nums, i-1, j, k)
            self.checkSum(nums, i, j, k+1)
            return 
        if (nums[i] + nums[j] + nums[k] > 0):
            self.checkSum(nums, i-1, j, k)
        else: 
            self.checkSum(nums, i, j, k+1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.finalList = []
        nums.sort()
        for j in range(1,(len(nums) - 1)):
            print(j)
            #j is mid index, getting k and i indices
            i = j - 1
            k = j + 1
            self.checkSum(nums, i, j, k)
            
                

        return self.finalList