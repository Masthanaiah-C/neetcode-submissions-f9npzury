class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # readSet = set()
        # a = None
        # b = None
        # for n in nums:
        #     print(readSet)
        #     if ((target - n) not in readSet):
        #         readSet.add(n)
        #     else:
        #         a =  target - n
        #         b = n
        #         break
        
        # print(a,b)
        # indexA = nums.index(a)
        # indexB = nums[indexA+1:].index(b)
        # return [indexA, indexA+1+indexB]

        seen = dict()
        for i in range(len(nums)):
            if ((target - nums[i]) in seen):
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        

       
