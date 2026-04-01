class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        max_left = height[0]
        max_right = height[n-1]
        leftheights = [max_left]
        rightheights = [max_right]
        waterTrapped = 0
        for index in range(1,n):
            if (height[index]>max_left):
                max_left = height[index]
            leftheights.append(max_left)
            if(height[n-1-index]>max_right):
                max_right = height[n-1-index]
            rightheights.append(max_right)
        print(leftheights, rightheights)
        for index in range(n):
            waterTrapped += (min(rightheights[n-1-index], leftheights[index]) - height[index])
        
        return waterTrapped