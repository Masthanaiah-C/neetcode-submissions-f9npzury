
class MinStack:

    def __init__(self):
        self.myList = list()
        self.minList = list()

    def push(self, val: int) -> None:
        self.myList.append(val)
        if (len(self.minList)==0):
            self.minList.append(val)
        else:
            self.minList.append(min(val, self.minList[-1]))
    def pop(self) -> None:
        self.myList.pop()
        self.minList.pop()
    def top(self) -> int:
        return self.myList[-1]

    def getMin(self) -> int:
        return self.minList[-1]

