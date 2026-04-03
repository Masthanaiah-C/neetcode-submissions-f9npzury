class Solution:
    def simplifyPath(self, path: str) -> str:
        #Split the string with /
        splitStr = path.split('/')
        print(splitStr)

        finalpath = list()
        for s in splitStr:
            # Ignore the empty string, even .
            if (s == '' or s == '.'):
                continue
            if (s == '..' ):
                if (len(finalpath)):
                    finalpath.pop()
                continue
            finalpath.append(s)

        return '/'+'/'.join(finalpath)