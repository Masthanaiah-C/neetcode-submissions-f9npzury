class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base Cases
        if (k == len(arr)):
            return arr
        
        
        left = 0
        right = len(arr) - 1
        indextoStart = -1
        while (left < right):
            mid = left + right
            mid = mid//2
            if (arr[mid] == x):
                indextoStart = mid
                break
            if (arr[mid] < x):
                left = mid+1
            else:
                right = mid-1 
        
        #index where to start with
        left = max(0, left-k)
        right = min( right+k, len(arr)-1)
        
        while(right-left+1 != k):
            if (abs(arr[left]-x) <= abs(arr[right]-x)):
                right-=1
            else:
                    left+=1
            
        print(left, right)
        return arr[left:right+1]
