class Solution:

    def encode(self, strs: List[str]) -> str:
        # Use a length-prefix with a delimiter to handle any character and empty lists
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find(":", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res