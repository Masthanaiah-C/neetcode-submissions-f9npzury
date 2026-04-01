class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestString = ""
        
        index = 0
        run = True
        while (run):
            match = True
            for s in strs:
                if (s == ""):
                    return ""
                if (index >= len(s)):
                    run = False
                    match = False
                    break
                if (s[index]!=strs[0][index]):
                    match = False
                    break
            if (match == False):
                break
            else:
                index+=1
            if (run == False):
                break
        return strs[0][:index]