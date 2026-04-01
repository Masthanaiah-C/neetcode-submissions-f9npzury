class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = ""
        for i in range(max(len(word1), len(word2))):
            if (i < len(word1)):
                finalString = finalString + word1[i]
            if (i < len(word2)):
                finalString = finalString + word2[i]
        return finalString
        