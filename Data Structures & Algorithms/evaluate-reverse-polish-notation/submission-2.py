class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        intStack = list()
        for token in tokens:
                print(intStack)
                if (token == "+"):
                    intStack.append(intStack.pop()+intStack.pop())
                    continue
                if (token == "-"):
                    b = intStack.pop()
                    a = intStack.pop()
                    intStack.append(a-b)
                    continue
                if (token == "*"):
                    b = intStack.pop()
                    a = intStack.pop()
                    intStack.append(a*b)
                    continue
                if (token == "/"):
                    b = intStack.pop()
                    a = intStack.pop()
                    intStack.append(int(a/b))
                    continue
                intStack.append(int(token))
        return intStack[0]
        