class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 1):
            if (nums[0]==target):
                return 0 
            else: 
                return -1
        
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = left + right
            mid = mid//2
            if (nums[mid] == target):
                return mid
            if (nums[mid] > target):
                if (target>=nums[left] ):
                    right = right - 1
                else:
                    left = left + 1
            else:
                if (target<=nums[right]):
                    left =left+ 1
                else:
                    right = right -1
            
        return -1