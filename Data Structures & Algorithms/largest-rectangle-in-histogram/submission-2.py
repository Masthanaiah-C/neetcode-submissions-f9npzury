class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        myStack = list()
        Area = 0
        cindex = 0
        dindex = 0

        for index in range(len(heights)):
            print(myStack, index, Area)
            if(len(myStack) == 0):
                myStack.append([heights[index], cindex, dindex])
                continue
            cindex = index
            dindex = index
            # top element is larger than current element
            while (myStack[-1][0] > heights[index]):
                top = myStack.pop()
                Area = max(Area, top[0]* (top[2]-top[1]+1))
                cindex = top[1]
                dindex = index
                if(len(myStack)==0):
                    myStack.append([heights[index], cindex, dindex])
                    break
            # top element is smaller than current element
            if (myStack[-1][0] < heights[index]):
                myStack.append([heights[index], cindex, dindex])
                continue
            # top element is equal to current element
            if (myStack[-1][0] == heights[index]):
                myStack[-1][2] = dindex
        print(myStack) 
        while (len(myStack)):
            top = myStack.pop()
            Area = max(Area, top[0]* (top[2]-top[1]+1)) 
            if (len(myStack)):
                myStack[-1][2] = top[2]
            print(myStack, Area)
        heights = heights[-1::-1]
        cindex = 0
        dindex = 0

        for index in range(len(heights)):
            print(myStack, index, Area)
            if(len(myStack) == 0):
                myStack.append([heights[index], cindex, dindex])
                continue
            cindex = index
            dindex = index
            # top element is larger than current element
            while (myStack[-1][0] > heights[index]):
                top = myStack.pop()
                Area = max(Area, top[0]* (top[2]-top[1]+1))
                cindex = top[1]
                if(len(myStack)==0):
                    myStack.append([heights[index], cindex, index])
                    break
                else:
                    myStack[-1][2]=top[2]
            # top element is smaller than current element
            if (myStack[-1][0] < heights[index]):
                myStack.append([heights[index], cindex, dindex])
                continue
            # top element is equal to current element
            if (myStack[-1][0] == heights[index]):
                myStack[-1][2] = dindex
        print(myStack) 
        while (len(myStack)):
            top = myStack.pop()
            Area = max(Area, top[0]* (top[2]-top[1]+1)) 
            if (len(myStack)):
                myStack[-1][2] = top[2]
            print(myStack, Area)
        return Area