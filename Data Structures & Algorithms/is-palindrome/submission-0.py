class Solution:
    def isAlpha(self, char ) -> bool:
        return (char >= "A" and char <="Z") or (char >= "a" and char <="z") or (char >= "0" and char <="9")

    def isPalindrome(self, s: str) -> bool:
        initialIndex = 0
        lastIndex = len(s) -1
        s = s.lower()
        while (initialIndex < lastIndex):
            if(not self.isAlpha(s[initialIndex])):
                initialIndex += 1
                continue
            if(not self.isAlpha(s[lastIndex])):
                lastIndex -= 1
                continue
            if (s[initialIndex] != s[lastIndex]):
                return False
            else:
                initialIndex += 1
                lastIndex -= 1
        return True