class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mapElements = dict()
        finalList = []
        for num in nums:
            if num not in mapElements.keys():
                mapElements[num] = 1
            else:
                mapElements[num] += 1
        for key, value in mapElements.items():
            if (value > (n // 3)):
                finalList.append(key)
        return finalList