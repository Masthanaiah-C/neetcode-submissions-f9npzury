class Solution:
    def isValid(self, st):
        if(len(st)==1):
            return True
        if(st[0]=='0'):
            return False
        if(int(st)>255 or len(st)>3):
            return False
        return True


    def restoreIpAddresses(self, s: str) -> List[str]:
        if (len(s) < 4):
            return []
        if (len(s) == 4):
            return ['.'.join(list(s))]
        myList = list()
        #more than 4 
        for i in range(1,min(4, len(s)-2)):
            print(i)
            if (not self.isValid(s[0:i])):
                continue
            for j in range(i+1,min(i+4, len(s)-1)):
                if (not self.isValid(s[i:j])):
                    continue
                for k in range(j+1, min(j+4,len(s))):
                    if (not self.isValid(s[j:k])):
                        continue
                    if (not self.isValid(s[k:len(s)])):
                            continue
                    print(i,j,k)
                    myList.append(s[0:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])

              


        
        return myList
