class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = ""
        len_w1 = len(word1)
        len_w2 = len(word2)
        for i in range(max(len_w1, len_w2)):
            if (i < len_w1):
                finalString = finalString + word1[i]
            if (i < len_w2):
                finalString = finalString + word2[i]
        return finalString
        