class Solution:
    def sumofDigits(self, n)->int:
        sum = 0
        while(n):
            sum += (n%10)*(n%10)
            n = n//10
        return sum
    def isHappy(self, n: int) -> bool:
        seen = list()
        while(n!=1):
            n = self.sumofDigits(n)
            if (n in seen):
                return False
            else:
                seen.append(n)
        return True
        