class Solution:
    def subsetPalindrome(self, s:str) -> bool:
        print(s)
        leftIndex = 0
        rightIndex = len(s) - 1
        isPalindrome = True
        while (leftIndex <= rightIndex):
            if (s[leftIndex] == s[rightIndex]):
                leftIndex += 1
                rightIndex -= 1
            else:
                isPalindrome = False
                break
        return isPalindrome
    def validPalindrome(self, s: str) -> bool:
        # finding odd character skip that index using two pointer
        leftIndex = 0
        rightIndex = len(s) - 1
        isPalindrome = True
        while (leftIndex <= rightIndex):
            if (s[leftIndex] == s[rightIndex]):
                leftIndex += 1
                rightIndex -= 1
            else:
                isPalindrome = False
                break
        if (not isPalindrome):
             return self.subsetPalindrome(s[leftIndex+1:rightIndex+1]) or self.subsetPalindrome(s[leftIndex:rightIndex])
        return isPalindrome
        # skip the right index and find the remaining inner one is palindrome
        # skip the left index and find the remaining inner one is palindrome.

