class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myResult = [0]*len(temperatures)
        myStack = [0]
        for i in range(1, len(temperatures)):
            if(temperatures[myStack[-1]] >= temperatures[i]):
                myStack.append(i)
            else:
                while(len(myStack) and temperatures[myStack[-1]] < temperatures[i]):
                    myResult[myStack[-1]] = i - myStack[-1]
                    myStack.pop()
                myStack.append(i)
        return myResult