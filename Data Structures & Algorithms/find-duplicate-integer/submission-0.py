class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force method
        # Check every pair of the number and see if they are equal 
        # atleast one of them will match return that integer
        # n^2 & o(1)

        # Sorting method
        # check adjacent values. 
        # n ^ log(n) & o(1)

        # set/hashmaps
        # check every time if an integer is in set
        # o(n) & o(n)

        # Using the constraint range[1,n]
        initial = nums[0]
        # put initial to the index position until. initial is equal to the value at index
        while (initial != nums[initial]):
            temp = nums[initial]
            nums[initial] = initial
            initial = temp
        
        return initial

