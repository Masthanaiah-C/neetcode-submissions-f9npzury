class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        start = 0
        end = len(nums)-k-1
        while (start<end):
            print(start,end)
            n = nums[start]
            nums[start] = nums[end]
            nums[end]  =n
            start+=1
            end-=1
        print(nums)
        start = len(nums)-k
        end = len(nums)-1
        while (start<end):
            n = nums[start]
            nums[start] = nums[end]
            nums[end]  =n
            start+=1
            end-=1
        start = 0
        end = len(nums)-1
        print(nums)
        while (start<end):
            n = nums[start]
            nums[start] = nums[end]
            nums[end]  =n
            start+=1
            end-=1

        