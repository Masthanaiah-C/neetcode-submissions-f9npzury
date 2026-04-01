class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string in ascending order
        # put them in set to find the unique str that become keys to the dictionary

        # for each key in set assign empty list 
        # then run through the string and add to the dictionary

        # club to optimize both

        finalAnagramList = dict()
        uniqueAnagram = set()

        for s in strs:
            sSorted = ''.join(sorted(s))
            if sSorted in uniqueAnagram:
                finalAnagramList[sSorted].append(s)
            else:
                finalAnagramList[sSorted] = [s]
                uniqueAnagram.add(sSorted)
        
        return list(finalAnagramList.values())
