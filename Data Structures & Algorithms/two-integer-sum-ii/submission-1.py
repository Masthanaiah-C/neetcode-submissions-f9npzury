class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1

        while(i<j):
            summ = numbers[i] + numbers[j]
            if(numbers[i] + numbers[j] == target):
                return [i+1,j+1]
            if(summ > target):
                j -=1
            else:
                i+=1
        return [j,i]