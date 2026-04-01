class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0
        
        ascii_dict = {chr(i): -1 for i in range(32, 127)}
        start_index = 0
        end_index = 0
        longstr = 1
        for index in range(len(s)):
            if (ascii_dict[s[index]] == -1):
                ascii_dict[s[index]] = index
                end_index = index
                longstr = max(longstr,end_index - start_index + 1)
            else:
                # longstr = max(longstr,end_index - start_index + 1)
                for ind in range(start_index, ascii_dict[s[index]]):
                    ascii_dict[s[ind]] = -1
                start_index = ascii_dict[s[index]] + 1
                ascii_dict[s[index]] = index
                end_index = index
            print(start_index, end_index, s[index],longstr)

        return longstr