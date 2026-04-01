class Solution:
    def swappostion(self, s :List[str], i: int, j: int):
        c = s[i]
        s[i] = s[j]
        s[j] = c
        return
    def reverseString(self, s: List[str]) -> None:
        for i in range((len(s)+1)//2):
            self.swappostion(s, i, len(s)-1-i)
        """
        Do not return anything, modify s in-place instead.
        """
        