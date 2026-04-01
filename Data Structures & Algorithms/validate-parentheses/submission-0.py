class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = list()
        match = dict()
        match["}"] = "{"
        match["]"] = "["
        match[")"] = "("
        for i in s:
            if i in ["{", "(", "["]:
                paranthesis.append(i)
            else:
                if ((len(paranthesis) ==0) or match[i] != paranthesis[-1]):
                    return False
                else: 
                    paranthesis.pop()
        if (len(paranthesis) == 0):
            return True
        else:
            return False