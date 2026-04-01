class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        while (result * result <= x):
            result+=1
        
        return result - 1
