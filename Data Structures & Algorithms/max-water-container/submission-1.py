class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxLeftHeight = [0]*n
        maxRightHeight = [0]*n
        
        for index in range(n):
            i = index
            if (maxLeftHeight[i] < heights[index]):
                maxLeftHeight[i] = heights[index]
            if (maxRightHeight[n-1-i] < heights[n-1-index]):
                maxRightHeight[n-1-i] = heights[n-1-index]
        
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
            

