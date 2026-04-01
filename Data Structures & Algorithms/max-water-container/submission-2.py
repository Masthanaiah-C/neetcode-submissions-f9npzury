class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        
        totalWater = 0
        leftIndex = 0
        rightIndex = n-1
        while (leftIndex < rightIndex):
            totalWater = max(totalWater, min(heights[leftIndex], heights[rightIndex])*(rightIndex - leftIndex))
            if(heights[leftIndex] > heights[rightIndex]):
                rightIndex-=1
            else:
                
                leftIndex+=1
        return totalWater
            

