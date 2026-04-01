class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        orgdict = dict()
        for s in s1:
            if (s in orgdict.keys()):
                orgdict[s] += 1
            else:
                orgdict[s] = 1

        s1len = len(s1)

        if (len(s2)< s1len):
            return False

        movdict = dict()

        for i in range(s1len):
            if (s2[i] in movdict.keys()):
                movdict[s2[i]] +=1
            else:
                movdict[s2[i]] =1
        
        if (orgdict == movdict):
            return True

        for j in range(s1len, len(s2)):
            movdict[s2[j - s1len]] -=1
            if (movdict[s2[j-s1len]] == 0):
                movdict.pop(s2[j-s1len])
            
            if (s2[j] in movdict.keys()):
                movdict[s2[j]] +=1
            else:
                movdict[s2[j]] = 1

            if( orgdict == movdict):
                return True

        return False


