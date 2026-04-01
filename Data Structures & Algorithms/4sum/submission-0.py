class Solution:
    def twoSum(self, nums, target, left, right):

        if(left>=right+1):
            return []
        List2Sum = list()
        while(left < right):
            sum2 = nums[left]+ nums[right]
            if(sum2== target):
                List2Sum.append([nums[left], nums[right]])
                left+=1
                right-=1
            else:
                if(sum2 > target):
                    right-=1
                else:
                    left+=1
        return List2Sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        finalList = []
        for i in range(n-3):
            for j in range(i+3, n):
                for pair in self.twoSum(nums, target - nums[i] - nums[j], i+1, j-1):
                    Sum4Set = [nums[i] , pair[0] , pair[1] , nums[j]]
                    if Sum4Set not in finalList:
                        finalList.append(Sum4Set)
        return finalList
